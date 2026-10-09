from django.urls import path

from . import views

app_name = 'PasswordCheck'
urlpatterns = [
    path('', views.index, name='index'),
    path('check_password/', views.evaluate_password, name='evaluate_password'),
]