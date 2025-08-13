from modeltranslation.translator import translator, TranslationOptions
from .models import Lead


class LeadTranslationOptions(TranslationOptions):
    fields = ('name', 'message')


translator.register(Lead, LeadTranslationOptions)
