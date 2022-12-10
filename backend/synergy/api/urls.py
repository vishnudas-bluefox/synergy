#!/usr/bin/env python3

from django.urls import path
from . import views

urlpatterns =[
    path('test/',views.test),
    path('classtest/',views.classtest),
    path('register/',views.registerview),
    path('login/',views.loginview),
    path('ksebsolarcapacity/',views.kseb_solarvalue),
]
