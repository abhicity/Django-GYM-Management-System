from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('', views.home, name='home'),
    # path("accounts/", include("django.contrib.auth.urls"),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='account_login'),
    # path('login/', auth_views.LoginView.as_view(template_name='gym/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('equipment/', views.equipment_list, name='equipment'),
    path('plans/', views.membership_plans, name='plans'),
    path('enquiry/', views.enquiry_form, name='enquiry'),



]