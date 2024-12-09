from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello, name='playground-home'),  # Root path of the playground namespace
    path('hello/', views.say_hello, name='playground-hello'),  # Hello path
]
