from django.contrib import admin
from django.urls import path
from article.views import index

urlpatterns = [
    path('hello/', index),
]
