from django.contrib import admin
from courses.models import  Course

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'school')
    list_filter = ('name','school')
    search_fields = ('name', 'description', 'school')