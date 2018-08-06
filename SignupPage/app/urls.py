from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.index),
    path('login',views.login),
    path('success', views.success),
]
