from django.urls import path
from article.views import *

urlpatterns = [
    path('topics/', TopicListView.as_view(), name='topic_list'),
    path('topics_list/', get_topic_list, name='function_topic_list'),
    path('create/', create_topic),
    path('create/form', TopicFormView.as_view()),
    path('update/', update_topic),
    path('delete/', delete_topic),
]
