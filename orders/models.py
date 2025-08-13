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

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("ID заказа")
    )
    number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("Номер заказа")
    )
    customer_name = models.CharField(
        max_length=255,
        verbose_name=_("Имя клиента")
    )
    phone = models.CharField(
        max_length=50,
        verbose_name=_("Телефон")
    )
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name=_("Email")
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Примечание")
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name=_("Статус заказа")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Дата создания")
    )
    paid_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("Дата оплаты")
    )

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name=_("Сумма заказа")
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name=_("Итоговая сумма")
    )

    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")

    def __str__(self):
        return self.number


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name=_("Заказ")
    )
    product_id = models.IntegerField(verbose_name=_("ID продукта"))
    title_snapshot = models.CharField(max_length=255, verbose_name=_("Название продукта"))
    qty = models.PositiveIntegerField(verbose_name=_("Количество"))
    unit_price_snapshot = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Цена за единицу"))

    class Meta:
        verbose_name = _("Элемент заказа")
        verbose_name_plural = _("Элементы заказа")

    def __str__(self):
        return f"{self.title_snapshot} ({self.qty})"
