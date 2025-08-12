from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', _("Новый")),
        ('in_progress', _("В работе")),
        ('paid', _("Оплачен")),
        ('cancelled', _("Отменён")),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(blank=True, null=True)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")

    def __str__(self):
        return self.number


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_id = models.IntegerField()
    title_snapshot = models.CharField(max_length=255)
    qty = models.PositiveIntegerField()
    unit_price_snapshot = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Элемент заказа")
        verbose_name_plural = _("Элементы заказа")
