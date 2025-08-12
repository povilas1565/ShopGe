from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    filterset_class = ProductFilter


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
