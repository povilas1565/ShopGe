from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Product, ProductImage, Category
from . import translation


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):  # вместо ModelAdmin
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(TranslationAdmin):  # вместо ModelAdmin
    list_display = ['title', 'price', 'in_stock', 'is_active']
    list_filter = ['is_active', 'category']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]
