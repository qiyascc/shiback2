from modeltranslation.translator import translator, TranslationOptions
from .models import Partner

class PartnerTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Partner, PartnerTranslationOptions)
