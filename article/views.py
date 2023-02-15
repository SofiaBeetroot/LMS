from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. Greetings from Beetroot Academy!")


def index(request):
    context = {'range': range(1, 6)}
    return render(request, 'courses.html', context)
