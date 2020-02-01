from django.contrib import admin
from .models import Profile, Role
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'education', 'mail', 'role',)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Role, RoleAdmin)
