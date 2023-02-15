from django.shortcuts import render
from django.http import HttpResponse
from article.models import Topic


# def index(request):
#     return HttpResponse("Hello, world. Greetings from Beetroot Academy!")


def get_topic_list(request):
    context = {'topic_list': Topic.objects.all()}
    return render(request, 'courses.html', context)
