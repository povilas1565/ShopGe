from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_("Название категории")
    )
    slug = models.SlugField(
        unique=True,
        max_length=120,
        verbose_name=_("Slug")
    )

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_("Название")
    )
    slug = models.SlugField(
        unique=True,
        max_length=255,
        verbose_name=_("Slug")
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("Описание")
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Цена")
    )
    in_stock = models.IntegerField(
        default=0,
        verbose_name=_("В наличии")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Активен")
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="products",
        verbose_name=_("Категория")
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Дата обновления")
    )

    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")

    def __str__(self):
        return self.title

