from rest_framework import serializers
from .models import Product, ProductImage, Category


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = serializers.CharField(source='category.title', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'description', 'price', 'in_stock', 'is_active', 'images', 'category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']
