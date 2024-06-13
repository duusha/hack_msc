from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('auth/', views.auth_view, name='auth'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
]

