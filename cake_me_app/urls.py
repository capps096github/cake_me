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

    # Users
    path("users", views.users, name="users"),

    # add user
    path("add_user", views.add_user, name="add_user"),

    # add_cakes
    path("add_cakes", views.add_cakes, name="add_cakes"),

    # delete cake
    path("delete_cake/<int:cake_id>", views.delete_cake, name="delete_cake"),


    # cart
    path("add/<int:cake_id>/", views.add_to_cart, name="cart_add"),
    path("remove/<int:cake_id>/", views.remove_from_cart, name="cart_remove"),
    path("details/<int:cake_id>/", views.details, name="details"),

    # check_out
    path("check_out", views.check_out, name="check_out"),

    # send email
    path("send_email", views.send_email, name="send_email"),

    # update_quantity in cart
    path("update_quantity/<int:item_id>/",
         views.update_quantity, name="update_quantity"),

    # adding cakes to the db
    path('cakes/', views.add_cakes, name='cakes'),

]


# For the "shop" it will then appear as http://127.0.0.1:8000/cake_me/shop/
