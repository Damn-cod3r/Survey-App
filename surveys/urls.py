
from django.urls import path
from . import views
app_name = "surveys"
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('signout/', views.signout, name='signout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('fromscratch/', views.fromscratch, name='fromscratch'),  
    path('survey_detail/<int:survey_id>/', views.survey_detail, name='survey_detail'), 
]
