from modeltranslation.translator import register, TranslationOptions
from .models import OrderItem


@register(OrderItem)
class OrderItemTranslationOptions(TranslationOptions):
    fields = ('title_snapshot',)
