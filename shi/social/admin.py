from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import SocialMedia
from .translation import SocialMediaTranslationOptions
from modeltranslation.translator import translator


@admin.register(SocialMedia)
class SocialMediaAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
    list_display = ('name', 'icon_preview')
    search_fields = ('name',)

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="width: 30px; height: 30px;" />', obj.icon.file.url)
        return "No Icon"

    icon_preview.short_description = "Social Media Icon"

