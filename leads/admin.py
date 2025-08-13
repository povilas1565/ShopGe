from django.contrib import admin
from django.utils.translation import gettext_lazy as _, get_language
from .models import Lead
import csv
from django.http import HttpResponse


@admin.action(description=_("Mark as processed"))
def mark_processed(request, queryset):
    queryset.update(processed=True)


@admin.action(description=_("Export selected leads to CSV"))
def export_leads_csv(request, queryset):
    current_lang = get_language()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="leads.csv"'
    writer = csv.writer(response)
    writer.writerow([_('Name'), _('Phone'), _('Source'), _('Message'), _('Date')])
    for lead in queryset:
        message_field = f"message_{current_lang}" if hasattr(lead, f"message_{current_lang}") else "message"
        name_field = f"name_{current_lang}" if hasattr(lead, f"name_{current_lang}") else "name"
        writer.writerow([
            getattr(lead, name_field, lead.name),
            lead.phone,
            lead.source,
            getattr(lead, message_field, lead.message) or '',
            lead.created_at,
        ])
    return response


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'source', 'created_at', 'processed']
    list_filter = ['processed', 'source', 'created_at']
    search_fields = ['name', 'phone', 'message']
    actions = [mark_processed, export_leads_csv]
    verbose_name = _("Лид")
    verbose_name_plural = _("Лиды")
