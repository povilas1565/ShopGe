from django.contrib import admin
from django.utils.translation import gettext_lazy as _, get_language
from django.utils.timezone import now
from django.http import HttpResponse
import csv
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ['product_id', 'title_snapshot', 'qty', 'unit_price_snapshot']
    extra = 0
    can_delete = False


@admin.action(description=_("Set as in progress"))
def set_in_progress(request, queryset):
    queryset.update(status='in_progress')


@admin.action(description=_("Set as paid and set paid date"))
def set_paid(request, queryset):
    queryset.update(status='paid', paid_at=now())


@admin.action(description=_("Cancel order"))
def set_cancelled(request, queryset):
    queryset.update(status='cancelled')


@admin.action(description=_("Export selected orders to CSV"))
def export_orders_csv(request, queryset):
    current_lang = get_language()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'
    writer = csv.writer(response)
    writer.writerow(
        [_('Number'), _('Customer Name'), _('Phone'), _('Email'), _('Status'), _('Created At'), _('Paid At'),
         _('Total')])
    for order in queryset:
        customer_field = f"customer_name_{current_lang}" if hasattr(order,
                                                                    f"customer_name_{current_lang}") else "customer_name"
        writer.writerow([
            getattr(order, customer_field, order.customer_name),
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
    verbose_name = _("Заказ")
    verbose_name_plural = _("Заказы")
