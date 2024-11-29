from django.contrib import admin
from .models import Media
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .translation import MediaTranslationOptions
from modeltranslation.translator import translator


@admin.register(Media)
class MediaAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)
