from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.world, name="world"),
    path("hello/<str:name>", views.hello, name="hello"),
]