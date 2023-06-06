from . import views
from django.urls import path

urlpatterns = [
    path('', views.market_index, name='market_index'),
    path('user_btn/', views.user_btn, name='user_btn'),
    path('love_btn/', views.love_btn, name='love_btn'),
    path('user_interface/', views.user_interface, name='user_interface'),
    path('create/', views.create, name='create'),
    path('create_interface/', views.create_interface, name='create_interface'),
    path('category/<str:option>/', views.category, name='category'),
    path('love/<idx>/', views.love_item, name='love_item'),
    path('remove/<idx>/', views.remove_item, name='remove_item'),
    path('preview/<idx>/', views.preview_item, name='preview_item'),
    path('comment/<idx>/', views.comment, name='comment'),
    path('search/', views.search_interface, name='search_interface')
]
