from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.index),
    path('login',views.login_view),
    path('success', views.success),
    path('home', views.home_view)
]

