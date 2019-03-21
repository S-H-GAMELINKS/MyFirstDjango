from djando.urls import path
from . import views

urlpattern = [
    path('', views.index, name='index'),
]