from django.contrib import admin
from .models import Service, Tag, Progress
from media.models import Media
from .translation import ServiceTranslationOptions
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline


class TagInline(admin.TabularInline):
    model = Service.tags.through  # Use the through table to manage the Many-to-Many relationship
    extra = 1  # One extra form for adding a new tag

class ServiceAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
    list_display = ('name', 'title', 'icon_preview')
    search_fields = ('name', 'title', 'description')
    inlines = [TagInline]  # Add inline for tags

    # Display icon in the admin panel
    def icon_preview(self, obj):
        if obj.icon:
            return f'<img src="{obj.icon.file.url}" style="width: 50px; height: 50px;" />'
        return "No Icon"
    
    icon_preview.short_description = "Icon"
    icon_preview.allow_tags = True

admin.site.register(Service, ServiceAdmin)
admin.site.register(Tag)

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'description')
    # list_editable = ('order',)
    ordering = ('order',)  # Ensure admin panel orders by 'order'