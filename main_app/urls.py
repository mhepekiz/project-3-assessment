from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_wacky, name='add_wacky'),
    path('delete/<int:id>/', views.delete_wacky, name='delete_wacky'),
]