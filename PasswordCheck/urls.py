from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='password_checker'),
    path('check_password/', views.evaluate_password, name='evaluate_password'),
]