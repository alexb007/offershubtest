from django.contrib import admin
from django.urls import path

admin.site.site_header = "OffersHubAdmin"
admin.site.site_title = "OffersHubAdmin"
admin.site.index_title = "OffersHubAdmin"

urlpatterns = [
    path('admin/', admin.site.urls),
]
