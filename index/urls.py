from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'), 
    path('index/', views.index, name='home'),
    path("create/", views.create_campaign, name='create_campaign'),
    path('market/', views.market_index, name='market_index'),
]
