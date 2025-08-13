from modeltranslation.translator import translator, TranslationOptions
from .models import OrderItem


class OrderItemTranslationOptions(TranslationOptions):
    fields = ('title_snapshot',)


translator.register(OrderItem, OrderItemTranslationOptions)
