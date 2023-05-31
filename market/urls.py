from . import views
from django.urls import path

urlpatterns = [
    path('', views.market_index, name='market_index'),
    path('user/', views.user_interface, name='user'),
    path('create/', views.create, name='create'),
    path('create_interface/', views.create_interface, name='create_interface'),
    
]
