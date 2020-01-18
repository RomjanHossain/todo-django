from django.urls import path
from . import views


urlpatterns = [
    path('views/', views.home, name='home'),
    path('', views.base, name='base'),
]
