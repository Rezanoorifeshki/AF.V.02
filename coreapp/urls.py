from django.contrib import admin
from django.urls import path
from . import views

app_name = 'coreapps'
urlpatterns = [
    path('', views.index, name='indexs'),
    path('about/', views.about, name='abouts'),
    path('contact/', views.contact, name='contacts'),
]