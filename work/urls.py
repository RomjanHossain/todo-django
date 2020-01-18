from django.urls import path
from . import views


urlpatterns = [
    path('views/', views.home, name='home'),
    path('', views.base, name='base'),
    path('delete/<do_id>', views.delete, name='delete'),
    path('complete/<id>', views.complete, name='complete'),
    path('edit/<id>', views.edit, name="edit"),
]
