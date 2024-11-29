from modeltranslation.translator import translator, TranslationOptions
from .models import SocialMedia
# Translation for the SocialMedia name field
class SocialMediaTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(SocialMedia, SocialMediaTranslationOptions)