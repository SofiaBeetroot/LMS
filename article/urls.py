from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from article.views import index

urlpatterns = [
    path('hello/', index),
]
