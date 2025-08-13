from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter


class ProductListAPIView(generics.ListAPIView):
    """Список активных товаров"""
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    permission_classes = [AllowAny]


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """Детальная информация о товаре"""
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
