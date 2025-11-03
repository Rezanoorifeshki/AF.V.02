from django.contrib import admin
from django.urls import path
from . import views

app_name = 'shopapps'

urlpatterns = [
    path('', views.shop, name='shops'),
    path('shopproduct/', views.shopproduct, name='shopproducts'),
]