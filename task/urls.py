from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add, name='add'),
    path('delete_todo/<str:pk>/', views.delete, name='delete'),
]