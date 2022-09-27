from django.contrib import admin

# import the models from models.py
from .models import Cake, Order, OrderItem


# register the Cake model
admin.site.register(Cake)

# register the Order model
admin.site.register(Order)

# register the OrderItem model
admin.site.register(OrderItem)

# Create superuser for the CakeMe project as per
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site

# Current superuser
# Username:  baker@cakeme
# Email address:  baker@cakeme.cake
# Password:  CakeMe@Baker096


# Current superuser
# Username:  cephas
# Email address:  cephasx@gmail.com
# Password:  Olga@Django096
