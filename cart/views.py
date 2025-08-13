from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from catalog.models import Product
from django.shortcuts import get_object_or_404


def get_cart(request):
    """Возвращает корзину текущего пользователя или гостя"""
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
    else:
        guest_id = request.session.session_key
        if not guest_id:
            request.session.create()
            guest_id = request.session.session_key
        cart, _ = Cart.objects.get_or_create(guest_id=guest_id)
    return cart


class CartAPIView(APIView):
    """Получить содержимое корзины"""
    permission_classes = [AllowAny]
    serializer_class = CartSerializer

    def get(self, request):
        cart = get_cart(request)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class CartItemCreateAPIView(APIView):
    """Добавить товар в корзину"""
    permission_classes = [AllowAny]
    serializer_class = CartItemSerializer

    def post(self, request):
        cart = get_cart(request)
        product_id = request.data.get('product_id')
        qty = int(request.data.get('qty', 1))

        product = get_object_or_404(Product, id=product_id, is_active=True)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'unit_price_snapshot': product.price, 'qty': qty}
        )
        if not created:
            cart_item.qty += qty
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartItemUpdateAPIView(APIView):
    """Обновить количество товара в корзине"""
    permission_classes = [AllowAny]
    serializer_class = CartItemSerializer

    def patch(self, request, pk):
        cart = get_cart(request)
        cart_item = get_object_or_404(CartItem, id=pk, cart=cart)
        qty = int(request.data.get('qty', cart_item.qty))
        if qty < 1:
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        cart_item.qty = qty
        cart_item.save()
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)


class CartItemDeleteAPIView(APIView):
    """Удалить товар из корзины"""
    permission_classes = [AllowAny]

    def delete(self, request, pk):
        cart = get_cart(request)
        cart_item = get_object_or_404(CartItem, id=pk, cart=cart)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
