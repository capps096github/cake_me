from django.urls import path

from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('shop/', views.shop, name='shop')
]


# For the "shop" it will then appear as http://127.0.0.1:8000/cake_me/shop/

