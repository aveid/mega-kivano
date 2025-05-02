from django.urls import path

from category.views import (CategoryListAPIView,
                            CategoryDetailAPIView,
                            CategoryCreateAPIView,
                          )

urlpatterns = [
    path("", CategoryListAPIView.as_view()),
    path("<str:title>/", CategoryDetailAPIView.as_view()),
    path("create/", CategoryCreateAPIView.as_view()),

]
