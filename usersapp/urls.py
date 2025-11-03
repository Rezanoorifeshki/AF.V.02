from django.contrib import admin
from django.urls import path
from . import views

app_name = 'usersapps'

urlpatterns = [
    path('', views.account, name='accounts'),
    path('login/', views.login, name='logins'),
]