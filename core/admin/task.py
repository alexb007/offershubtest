from django.contrib import admin

from core.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('gid', 'name', 'completed_by')
    list_filter = ('projects', 'completed_by')
    list_display_links = ('gid', 'name', 'completed_by')
    search_fields = ('gid', 'name', 'projects__name')
    readonly_fields = ('gid', )
