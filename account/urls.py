from django.contrib import admin
from django.urls import path
from account.views import *

urlpatterns = [
    path('login/', sing_in),
    path('logout/', sing_out),
    path('registration/', registration)
]
