from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='home'),
    path('form/', views.client_form_view, name='form'),
]
