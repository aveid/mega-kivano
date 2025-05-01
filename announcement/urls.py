from django.urls import path
from announcement import views

urlpatterns = [
    path("", views.CreateItemAPIView.as_view()),
]