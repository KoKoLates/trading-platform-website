from . import views
from django.urls import path

urlpatterns = [
    path('', views.market_index, name='market_index'),
]

