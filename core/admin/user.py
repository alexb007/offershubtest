from django.contrib import admin

from core.models import AsanaUser


@admin.register(AsanaUser)
class AsanaUserAdmin(admin.ModelAdmin):
    list_display = ('gid', 'name')
    list_display_links = ('gid', 'name')
    search_fields = ('gid', 'name')
    readonly_fields = ('gid', )
