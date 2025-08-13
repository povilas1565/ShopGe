from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from catalog.models import Product


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь")
    )
    guest_id = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("ID гостя"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))

    class Meta:
        verbose_name = _("Корзина")
        verbose_name_plural = _("Корзины")


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name=_("Корзина")
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name=_("Товар")
    )
    qty = models.PositiveIntegerField(default=1, verbose_name=_("Количество"))
    unit_price_snapshot = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Цена за единицу"))

    class Meta:
        verbose_name = _("Элемент корзины")
        verbose_name_plural = _("Элементы корзины")
