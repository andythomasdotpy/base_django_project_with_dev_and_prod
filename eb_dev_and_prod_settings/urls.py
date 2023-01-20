from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("my_app_1.urls")),
    path("catch-me-if-you-can/", admin.site.urls),
]
