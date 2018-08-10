from django.urls import path

from . import views

app_name = 'myappp'
urlpatterns = [
    path('', views.index, name='index'),
]