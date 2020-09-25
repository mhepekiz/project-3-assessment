from django.urls import path
from . import views

urlpatterns = [
    path('', views.WackyCreate.as_view(), name='index'),
]