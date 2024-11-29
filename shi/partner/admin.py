from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import Partner
from .translation import PartnerTranslationOptions
from modeltranslation.translator import translator


@admin.register(Partner)
class PartnerAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
    list_display = ('name', 'image_preview')
    search_fields = ('name',)

    def image_preview(self, obj):
        if obj.image.file:
            return format_html('<img src="{}" style="width: 200px; height: auto;" />', obj.image.file.url)
        return "No Image - image yükləmək lazımdır bura emillll"

    image_preview.short_description = "Partner image"  


