from django.urls import path
from magazines import views

urlpatterns = [
    path("", views.add_magazine, name="add_magazine"),
]
