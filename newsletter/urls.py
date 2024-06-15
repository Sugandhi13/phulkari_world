""" Paths for newsletter app """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter, name='newsletter')
]