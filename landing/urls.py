from django.urls import path
from . import views

urlpatterns = [
    path('', views.goto_landing, name='landing'),
]