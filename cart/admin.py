from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('product', 'unit_price_snapshot')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_or_guest', 'created_at')
    inlines = [CartItemInline]
    verbose_name = _("Корзина")
    verbose_name_plural = _("Корзины")

    def user_or_guest(self, obj):
        return obj.user.username if obj.user else f'{_("Guest")}: {obj.guest_id}'

    user_or_guest.short_description = _('User/Guest')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'qty', 'unit_price_snapshot')
    readonly_fields = ('unit_price_snapshot',)
    verbose_name = _("Элемент корзины")
    verbose_name_plural = _("Элементы корзины")
