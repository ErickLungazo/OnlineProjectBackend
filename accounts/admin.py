from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'username', 'role', 'is_active')
    list_filter = ('role', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'role', 'is_active')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

    def save_model(self, request, obj, form, change):
        # Automatically assign groups based on role
        super().save_model(request, obj, form, change)
        if obj.role == 'admin':
            obj.groups.set(Group.objects.filter(name='Admins'))
        elif obj.role == 'lecturer':
            obj.groups.set(Group.objects.filter(name='Lecturers'))
        elif obj.role == 'student':
            obj.groups.set(Group.objects.filter(name='Students'))
        obj.save()


admin.site.register(CustomUser, CustomUserAdmin)
