from django.urls import path
from . import views as views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:user_id>/delete/', views.delete_view, name='delete'),
    path('<int:user_id>/profile/', views.profile, name='profile'),
    path('<int:user_id>/profile_update/', views.profile_update, name='profile_update'),
    path('<int:user_id>/pw_update/', views.pw_update, name='pw_update'),
]