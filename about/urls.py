# Importing libraries required to build url patterns

from django.urls import path
from . import views

# url configuration for about app

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('', views.about_us, name='about'),
]