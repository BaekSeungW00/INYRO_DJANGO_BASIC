from django.urls import path
from .import views as views

urlpatterns = [
    path('create/', views.post_create, name='post_create'),
    path('update/', views.post_update, name='post_update'),
    path('delete/', views.post_delete, name='post_delete'),
    path('list/', views.post_list_view, name='post_list'),
]
