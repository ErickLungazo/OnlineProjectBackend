from django.contrib import admin

from .models import Assessment, Paper


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'school',)
    list_filter = ('school',)
    search_fields = ('name',)


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit', 'assessment', 'created_at', 'updated_at')
    list_filter = ('unit', 'assessment',)
    search_fields = ('unit__name', 'assessment__name',)
