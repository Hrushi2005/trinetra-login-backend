from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),  # 👈 redirect root to /login/
    path('login/', views.login_view, name='login'),
    path('success/', views.success_view, name='success'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('employees/', views.employee_list_view, name='employees'),


]
