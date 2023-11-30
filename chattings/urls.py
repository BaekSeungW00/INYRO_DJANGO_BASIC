from django.urls import path
from . import views

urlpatterns = [
    path('chatting/', views.chat_view, name='chatting'),
]
