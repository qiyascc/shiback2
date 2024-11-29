from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import Project, Badge
from .translation import ProjectTranslationOptions, BadgeTranslationOptions


class BadgeInline(TranslationTabularInline):
    model = Badge
    extra = 1

@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
    inlines = [BadgeInline]
    list_display = ('name', 'year', 'client', 'industry')
    search_fields = ('name', 'client', 'industry')
    filter_horizontal = ('services', 'collaborators')  # For ManyToMany relationships
