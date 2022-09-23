from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('shop/', views.shop, name='shop'),
    # change the url to filter by category name in lower case and add the name of the url to the path function
    # e.g in format http://127.0.0.1:8000/cakex_app/?show=Soda
    # this can have a regex in the url too
    # a to z and A to Z regex
    re_path(r"^shop/(?:cakes=(?P<category>[a-zA-Z]+)/)?$", views.shop),

]


# For the "shop" it will then appear as http://127.0.0.1:8000/cake_me/shop/
