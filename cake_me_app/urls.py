from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('shop/', views.shop, name='shop'),
    # change the url to filter by category name in lower case and add the name of the url to the path function
    # e.g in format http://127.0.0.1:8000/cakex_app/?show=Soda
    # this can have a regex in the url to
    # a to z and A to Z regex
    re_path(r"^shop/(?:cakes=(?P<category>[a-zA-Z]+)/)?$", views.shop),

    # register
    path("register", views.register, name="register"),

    # search
    path("search", views.search, name="search"),

    # profile
    path("profile", views.profile, name="profile"),

    # cart
    path("add/<int:cake_id>/", views.add_to_cart, name="cart_add"),
    path("remove/<int:cake_id>/", views.remove_from_cart, name="cart_remove"),
    path("details/<int:cake_id>/", views.details, name="details"),
]


# For the "shop" it will then appear as http://127.0.0.1:8000/cake_me/shop/
