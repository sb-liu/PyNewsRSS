from django.contrib import admin
from django.urls import path, include
from generator import views

urlpatterns = [
    path('', views.index),
    path('/tags', views.tag_response)
]