from django.contrib.auth.admin import UserAdmin
from .models import Parent, Child
from django.contrib import admin
from django.contrib.auth.models import Group


class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ('id', )

    def get_permissions(self, obj):
        permissions = obj.permissions.all()
        return ', '.join([p.name for p in permissions])

    get_permissions.short_description = 'Permissions'


admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)


class UserAdmin(UserAdmin):
    model = Parent
    list_display = ('login', 'email', 'is_staff', 'is_active', 'role')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        ('Personal Info', {'fields': ('username', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'role', 'login', 'password', 'email')
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)


class ChildAdmin(admin.ModelAdmin):
    list_display = ('profile_picture', 'username', 'is_active')
    list_filter = ('is_active', )
    fieldsets = (
        ('Personal Info', {'fields': ('username', 'password', 'profile_picture',)}),
        ('Permissions', {'fields': ('is_active', )}),
    )


admin.site.register(Parent, CustomGroupAdmin)
admin.site.register(Child, ChildAdmin)
