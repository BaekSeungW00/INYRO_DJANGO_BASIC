from django.urls import path
from .import views as views

urlpatterns = [
    path('create/', views.post_create, name='post_create'),
    path('<int:post_id>/update/', views.post_update, name='post_update'),
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('list/', views.post_list_view, name='post_list'),
    path('<int:post_id>/detail/', views.post_detail, name="post_detail"),
    path('<int:post_id>/attachment/', views.post_attachment, name='post_attachment')
]   
