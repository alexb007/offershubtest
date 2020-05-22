from django.contrib import admin

from core.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('gid', 'name', 'synced')
    list_display_links = ('gid', 'name', 'synced')
    search_fields = ('gid', 'name')
    list_filter = ('synced', )
