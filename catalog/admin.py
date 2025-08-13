from django.contrib import admin
from django.utils.translation import get_language
from modeltranslation.admin import TranslationAdmin
from .models import Category, Product, ProductImage
from . import translation


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):  # TranslationAdmin берёт переводы автоматически
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['title', 'price', 'in_stock', 'is_active']
    list_filter = ['is_active', 'category']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]
