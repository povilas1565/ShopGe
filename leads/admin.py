from django.contrib import admin
from .models import Lead
from django.http import HttpResponse
import csv


@admin.action(description="Отметить как обработанные")
def mark_processed(request, queryset):
    queryset.update(processed=True)


@admin.action(description="Экспортировать выбранные лиды в CSV")
def export_leads_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="leads.csv"'
    writer = csv.writer(response)
    writer.writerow(['Имя', 'Телефон', 'Источник', 'Сообщение', 'Дата'])
    for lead in queryset:
        writer.writerow([
            lead.name,
            lead.phone,
            lead.source,
            lead.message or '',
            lead.created_at,
            ])
    return response


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'source', 'created_at', 'processed']
    list_filter = ['processed', 'source', 'created_at']
    search_fields = ['name', 'phone', 'message']
    actions = [mark_processed, export_leads_csv]
