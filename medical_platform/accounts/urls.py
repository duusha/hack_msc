from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('auth/', views.auth_view, name='auth'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('user/<int:user_id>/schedule/', views.user_schedule, name='user_schedule'),
    path('all_schedules/', views.all_schedules, name='all_schedules'),
]

