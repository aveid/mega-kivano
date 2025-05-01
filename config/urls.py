from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/categories/", include("category.urls")),
    path("api/v1/items/", include("announcement.urls")),
]
