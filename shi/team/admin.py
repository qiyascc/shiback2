from django.contrib import admin
from .models import TeamMember, TeamSocial, Gallery
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .translation import TeamMemberTranslationOptions



class TeamSocialInline(admin.TabularInline):
    model = TeamSocial
    extra = 1  # One extra empty form to add new social media account


class TeamMemberAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
    list_display = ('full_name', 'position', 'image_preview')
    search_fields = ('full_name', 'position')
    list_filter = ('position',)
    inlines = [TeamSocialInline] 

    # Display the icon for social media links
    def icon_preview(self, obj):
        icons = ""
        for sm in obj.social_media.all():
            if sm.icon:
                icons += format_html('<img src="{}" style="width: 20px; height: 20px; margin-right: 5px;" />', sm.icon.file.url)
        return icons or "No Icons"
    
    icon_preview.short_description = "Social Media Icons"

    # Capitalize position and format accordingly
    def save_model(self, request, obj, form, change):
        obj.position = obj.position.capitalize()  # Ensure first letter is capitalized and the rest are lowercase
        super().save_model(request, obj, form, change)

    # Image preview for admin panel
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: 100px;" />', obj.image.file.url)
        return "No Image"
    
    image_preview.short_description = "Profile Image"

class GalleryAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
    list_display = ('image_preview', 'description')
    search_fields = ('description',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.file.url}" style="width: 50px; height: 50px;" />'
        return "No Image"
    
    image_preview.short_description = "Gallery Image"
    image_preview.allow_tags = True

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)