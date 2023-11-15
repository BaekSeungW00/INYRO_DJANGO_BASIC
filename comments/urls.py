from django.urls import path
from . import views as views

urlpatterns = [
    path('create/', views.comment_create, name='comment_create'),
]