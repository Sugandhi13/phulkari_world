# Importing libraries required to build url patterns

from django.urls import path
from . import views

# url configuration for about app

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('add_faq/', views.add_faq, name='add_faq'),
    path('edit_faq/<int:faq_id>/', views.edit_faq, name='edit_faq'),
    path('faq/', views.faq, name='faq'),
    path(
        'delete/<int:faq_id>/',
        views.delete_faq,
        name='delete_faq'
        ),
    path('edit/', views.edit_about_us, name='edit_about_us'),
    path('', views.about_us, name='about'),
]