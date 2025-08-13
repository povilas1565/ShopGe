from modeltranslation.translator import translator, TranslationOptions

from .models import Product, Category


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Product, ProductTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
