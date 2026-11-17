from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producten/', views.producten, name='producten'),
    path('workshops/', views.workshops, name='workshops'),
    path('contact/', views.contact, name='contact'),
]
