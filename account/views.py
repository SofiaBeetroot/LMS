from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout

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