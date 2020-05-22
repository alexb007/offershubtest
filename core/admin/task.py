from django.contrib import admin

from core.admin.actions import sync_remote_selected
from core.models import Task




@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('gid', 'name', 'assignee', 'synced')
    list_filter = ('projects', 'assignee', 'synced')
    list_display_links = ('gid', 'name', 'assignee', 'synced')
    search_fields = ('gid', 'name', 'projects__name')
    readonly_fields = ('gid',)
    actions = (sync_remote_selected, )
