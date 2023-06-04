from . import views
from django.urls import path

urlpatterns = [
    path('', views.market_index, name='market_index'),
    path('user_btn/', views.user_btn, name='user_btn'),
    path('user_interface/', views.user_interface, name='user_interface'),
    path('create/', views.create, name='create'),
    path('create_interface/', views.create_interface, name='create_interface'),
    path('category/<str:option>/', views.category, name='category')
]
