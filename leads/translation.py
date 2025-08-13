from modeltranslation.translator import register, TranslationOptions
from .models import Lead


@register(Lead)
class LeadTranslationOptions(TranslationOptions):
    fields = ('name', 'message',)
