from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='name'),
    path('welcome/',views.welcome,name='welcome'),
    path('welcome/logout',views.logout,name='logout'),
]