import httpx
import asyncio
from time import sleep, perf_counter
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from asgiref.sync import sync_to_async, async_to_sync

from account.forms import LoginForm, RegistrationForm


class HomeView(TemplateView):
    template_name = 'base.html'


def sing_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=password)
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                return redirect('home')
    else:
        if request.user.is_authenticated:
            return redirect('home')
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def sing_out(request):
    logout(request)
    return redirect('home')


@sync_to_async
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'registration/registr.html', {'form': form})


async def index(request):
    return HttpResponse('Hello from async Django!')


async def http_call_async():
    start = perf_counter()
    for num in range(1, 6):
        await asyncio.sleep(1)
        # print(num)
    async with httpx.AsyncClient() as client:
        result = await client.get('https://httpbin.org/')
        # print(result)
    end = perf_counter()
    print('async', end - start, sep=' --- ')


def http_call_sync():
    start = perf_counter()
    for num in range(1, 6):
        sleep(1)
        # print(num)
    result = httpx.get('https://httpbin.org/')
    # print(result)
    end = perf_counter()
    print('sync', end - start, sep=' --- ')


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('Non-blocking request!')


def sync_view(request):
    http_call_sync()
    return HttpResponse('Blocking request!')


async def async_with_sync_view(request):
    loop = asyncio.get_event_loop()
    async_http = sync_to_async(http_call_sync, thread_sensitive=False)
    loop.create_task(async_http())
    return HttpResponse('Non-blocking request with sync function')


def sync_with_async_view(request):
    http_sync = async_to_sync(http_call_async)
    http_sync()
    return HttpResponse('Blocking request with async function')
