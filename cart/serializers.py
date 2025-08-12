from rest_framework import serializers
from .models import Cart, CartItem
from catalog.serializers import ProductSerializer
from catalog.models import Product  # обязательно импортируй модель


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.none(),  # пустой queryset по умолчанию
        source='product',
        write_only=True
    )

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'qty', 'unit_price_snapshot']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user if 'request' in self.context else None
        if user and hasattr(user, 'catalog_product_queryset'):
            self.fields['product_id'].queryset = user.catalog_product_queryset
        else:
            self.fields['product_id'].queryset = Product.objects.none()


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'guest_id', 'items']
