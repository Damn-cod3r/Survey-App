# urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
]
