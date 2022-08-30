# articles/urls.py

from django.urls import path
from . import views		

urlpatterns = [
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('dinner/', views.dinner),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<name>/', views.hello),
    path('num/<int:num>/', views.num),
]