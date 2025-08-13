from django.contrib import admin
from modeltranslation.admin import TranslationTabularInline
from .models import Order, OrderItem
from django.utils.translation import get_language
from django.utils.timezone import now
from django.http import HttpResponse
import csv
from . import translation


class OrderItemInline(TranslationTabularInline):
    model = OrderItem
    readonly_fields = ['product_id', 'title_snapshot', 'qty', 'unit_price_snapshot']
    extra = 0
    can_delete = False


@admin.action(description="Отметить как 'В работе'")
def set_in_progress(request, queryset):
    queryset.update(status='in_progress')


@admin.action(description="Отметить как 'Оплачено' и установить дату оплаты")
def set_paid(request, queryset):
    queryset.update(status='paid', paid_at=now())


@admin.action(description="Отменить заказ")
def set_cancelled(request, queryset):
    queryset.update(status='cancelled')


@admin.action(description="Экспортировать выбранные заказы в CSV")
def export_orders_csv(request, queryset):
    current_lang = get_language()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'
    writer = csv.writer(response)
    writer.writerow(['Номер', 'Имя клиента', 'Телефон', 'Email', 'Статус', 'Дата создания', 'Дата оплаты', 'Сумма'])
    for order in queryset:
        writer.writerow([
            order.number,
            getattr(order, f"customer_name_{current_lang}", order.customer_name),
            order.phone,
            order.email or '',
            order.status,
            order.created_at,
            order.paid_at or '',
            order.total,
        ])
    return response


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['number', 'customer_name', 'phone', 'status', 'created_at', 'paid_at', 'total']
    list_filter = ['status', 'created_at', 'paid_at']
    inlines = [OrderItemInline]
    actions = [set_in_progress, set_paid, set_cancelled, export_orders_csv]
