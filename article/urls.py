from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from article.views import *

urlpatterns = [
    path('topics/', get_topic_list),
    path('create/', create_topic),
    path('update/', update_topic),
    path('delete/', delete_topic)
]
