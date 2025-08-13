from modeltranslation.translator import register, TranslationOptions
from .models import CartItem


@register(CartItem)
class CartItemTranslationOptions(TranslationOptions):
    fields = ('unit_price_snapshot',)  # Обычно нет смысла, можно пропустить
