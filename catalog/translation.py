from modeltranslation.translator import register, TranslationOptions
from .models import Product, Category


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
