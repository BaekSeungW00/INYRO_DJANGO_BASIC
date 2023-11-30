from django.urls import path
from . import views as views

urlpatterns = [
    path('<int:post_id>/create/', views.comment_create, name='comment_create'),
    path('<int:post_id>/<int:comment_id>/upadate/', views.comment_update, name='comment_update'),
    path('<int:post_id>/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),

]