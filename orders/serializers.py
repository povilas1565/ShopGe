from abc import ABC

from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product_id', 'title_snapshot', 'qty', 'unit_price_snapshot']


class OrderCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField(required=False, allow_blank=True)
    comment = serializers.CharField(required=False, allow_blank=True)

    def validate_phone(self, value):
        if not value:
            raise serializers.ValidationError("Телефон обязателен.")
        return value


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'number', 'customer_name', 'phone', 'email', 'note', 'status', 'created_at', 'paid_at', 'subtotal', 'total', 'items']
