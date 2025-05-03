from django.urls import path

from users.views import RegisterUser

urlpatterns = [
    path("", RegisterUser.as_view()),
]