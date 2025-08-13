from modeltranslation.admin import TranslationTabularInline, TranslationAdmin
from .models import Cart, CartItem
from django.contrib import admin
from . import translation


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('product', 'unit_price_snapshot')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_or_guest', 'created_at')
    inlines = [CartItemInline]

    def user_or_guest(self, obj):
        return obj.user.username if obj.user else f'Guest: {obj.guest_id}'

    user_or_guest.short_description = 'User/Guest'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'qty', 'unit_price_snapshot')
    readonly_fields = ('unit_price_snapshot',)
