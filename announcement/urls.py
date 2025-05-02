from django.urls import path
from announcement import views

urlpatterns = [
    path("", views.CreateItemAPIView.as_view()),
    # path("<int:pk>/", views.ItemAPIView.as_view()),
    path("<str:sub_category>/", views.DetailSubCategoryAPIView.as_view()),

]