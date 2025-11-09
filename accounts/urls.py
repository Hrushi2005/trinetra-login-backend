from django.urls import path
from . import views

urlpatterns = [
    path('admin_login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('view_employees/', views.view_employees, name='view_employees'),
    path('api/user_login/', views.user_login, name='user_login_api'),

]
