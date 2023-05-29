
from . import views
from django.urls import path

urlpatterns = [
    path('', views.login_interface, name='login_interface'),
    path('login/', views.login_attempt, name='login'), 
    path('logout/', views.logout_attempt, name='logout'),
    path('register/', views.register, name='register'),
    ## password 
    path('token/', views.send_token, name='send_token'),
    path('verify/<token>', views.verify, name='verify'),
    path('forget-password/', views.forget_password, name='forget_password'), 
    path('change-password/<token>/', views.change_password, name='change_password'),
    ## error handling 
    path('error/', views.error, name='error')
]
