from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from article.views import get_topic_list

urlpatterns = [
    path('topics/', get_topic_list),
]
