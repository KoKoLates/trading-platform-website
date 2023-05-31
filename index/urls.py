from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'), 
    path('index/', views.index, name='home'),
    path('create/', views.create_campaign, name='create_campaign'),
    path('delete/<idx>/', views.delete_campaign, name='delete_campaign'),
    path('cancel/<idx>/', views.cancel_campaign, name='cancel_campaign'),
    path('register/<idx>/', views.register_campaign, name='register_campaign'),

    # transition to the market page
    path('market/', views.market_index, name='market_index'),
]
