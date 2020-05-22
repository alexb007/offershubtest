from django.contrib import admin

from core.admin.actions import sync_remote_selected
from core.models import AsanaUser


@admin.register(AsanaUser)
class AsanaUserAdmin(admin.ModelAdmin):
    list_display = ('gid', 'name', 'synced',)
    list_display_links = ('gid', 'name', 'synced',)
    list_filter = ('synced', )
    search_fields = ('gid', 'name')
    readonly_fields = ('gid', )
    actions = (sync_remote_selected,)
