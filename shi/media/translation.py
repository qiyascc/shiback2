from modeltranslation.translator import translator, TranslationOptions
from .models import Media

class MediaTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Media, MediaTranslationOptions)
