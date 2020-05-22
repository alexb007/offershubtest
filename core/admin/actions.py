def sync_remote_selected(modeladmin, request, queryset):
    for entry in queryset:
        entry.sync_remote()


sync_remote_selected.short_description = "Синхронизировать с Asana"
