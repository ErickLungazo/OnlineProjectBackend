# media/admin.py
from django.contrib import admin
from .models import Media


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at', 'file_type', 'file_size', 'original_filename')
    search_fields = ('original_filename',)
