from django.contrib import admin
from .models import CompanyName, About, WorkStatus

class CompanyNameAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not CompanyName.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(CompanyName, CompanyNameAdmin)


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not About.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(About, AboutAdmin)


class WorkStatusAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not WorkStatus.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(WorkStatus, WorkStatusAdmin)
