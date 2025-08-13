from django.db import models
from django.utils.translation import gettext_lazy as _


class Lead(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Имя")
    )
    phone = models.CharField(
        max_length=50,
        verbose_name=_("Телефон / Email")
    )
    source = models.CharField(
        max_length=50,
        verbose_name=_("Источник")
    )
    message = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Сообщение")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Дата создания")
    )
    processed = models.BooleanField(
        default=False,
        verbose_name=_("Обработан")
    )

    class Meta:
        verbose_name = _("Лид")
        verbose_name_plural = _("Лиды")

    def __str__(self):
        return f"{self.phone} ({self.source})"

