from django.contrib import admin
from django.urls import path, include

from loginapp import views

urlpatterns = [
    path('login/',views.login),
    path('logincheck/',views.logincheck)
]