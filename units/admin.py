from django.contrib import admin

from units.models import Unit


# Register your models here.
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')
    search_fields = ('name', 'course')
    list_filter = ('name', 'course')