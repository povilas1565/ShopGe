from rest_framework import status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.timezone import now
from django.db import transaction
from .models import Order, OrderItem
from cart.models import Cart
from .serializers import OrderCreateSerializer, OrderSerializer, EmptySerializer
from django.shortcuts import get_object_or_404
import uuid


def generate_order_number():
    return uuid.uuid4().hex[:12].upper()


class OrderCreateAPIView(views.APIView):
    """Создание нового заказа"""
    permission_classes = [AllowAny]
    serializer_class = OrderCreateSerializer

    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user).first()
        else:
            guest_id = request.session.session_key
            if not guest_id:
                request.session.create()
                guest_id = request.session.session_key
            cart = Cart.objects.filter(guest_id=guest_id).first()

        if not cart or not cart.items.exists():
            return Response({"detail": "Корзина пуста."}, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data

        with transaction.atomic():
            order = Order.objects.create(
                number=generate_order_number(),
                customer_name=data['name'],
                phone=data['phone'],
                email=data.get('email'),
                note=data.get('comment'),
                status='new',
            )
            subtotal = sum(item.unit_price_snapshot * item.qty for item in cart.items.all())
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product_id=item.product.id,
                    title_snapshot=item.product.title,
                    qty=item.qty,
                    unit_price_snapshot=item.unit_price_snapshot,
                )

            order.subtotal = subtotal
            order.total = subtotal
            order.save()
            cart.items.all().delete()

        return Response({"order_number": order.number, "status": order.status}, status=status.HTTP_201_CREATED)


class OrderSetInProgressAPIView(views.APIView):
    """Перевести заказ в статус 'в работе'"""
    permission_classes = [AllowAny]
    serializer_class = EmptySerializer

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.status = 'in_progress'
        order.save()
        return Response({"status": order.status})


class OrderSetPaidAPIView(views.APIView):
    """Отметить заказ как оплаченный"""
    permission_classes = [AllowAny]
    serializer_class = EmptySerializer

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.status = 'paid'
        order.paid_at = now()
        order.save()
        return Response({"status": order.status, "paid_at": order.paid_at})


class OrderCancelAPIView(views.APIView):
    """Отменить заказ"""
    permission_classes = [AllowAny]
    serializer_class = EmptySerializer

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.status = 'cancelled'
        order.save()
        return Response({"status": order.status})
