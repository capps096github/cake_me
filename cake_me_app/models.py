from django.db import models
from django.urls import reverse
from django.utils import timezone

from django.contrib.auth.models import User

""" Cake Model with   
- name, description, price, image_url, category
"""


class Cake(models.Model):
    # name
    name = models.CharField(
        max_length=50, help_text='Enter the name of the cake')
    # description
    description = models.TextField(
        help_text='Enter the description of the cake')
    # price
    price = models.IntegerField(help_text='Enter the price of the cake')
    # image_url
    image_url = models.TextField(help_text='Enter the image url of the cake')
    # category
    category = models.CharField(
        max_length=50, help_text='Enter the category of the cake', default="Sponge")

    # we want to order our cakes by name, so we need to add a class Meta
    class Meta:
        ordering = ['name']

    # we can also get a url for our cake by its name in lower case in the detail view
    def get_absolute_url(self):
        return reverse('cake_detail', args=[str(self.name).lower()])

    def __str__(self):
        return f"Name: {self.name} - Description: {self.description} - Price: {self.price} - Image: {self.image_url} - Category: {self.category}"


""" OrderItem Model with
- cake_id(foreign key), quantity, order_id(foreign key)
"""


class CakeOrderItem(models.Model):
    # cake_id
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, default=1)

    # quantity
    quantity = models.IntegerField(
        help_text='Enter the quantity of the cake', default=0)

    def __str__(self):
        return f" * Cake: {self.cake.__str__()} - Quantity: {self.quantity}\n"


""" Order Model with
- userId as foreign key, total_cost, date
"""


class Order(models.Model):
    # userId
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # total_cost
    total_cost = models.FloatField(
        help_text='Enter the total cost of the order', default=0)
    # date
    date = models.DateField(
        help_text='Enter the date of the order', default=timezone.now)

    # order items
    items = models.ManyToManyField(CakeOrderItem)

    # update the total cost of the order
    def update_total_cost(self):
        self.total_cost = 0
        for item in self.items.all():
            self.total_cost += item.cake.price * item.quantity
        self.save()

    # get total price
    def get_total_price(self):
        return self.total_cost

    def __str__(self):
        # get strings of all the items in the order
        items = [item.__str__() for item in self.items.all()]

        return f"- Total Cost: {self.total_cost}\n - Date: {self.date}\n    - Items: \n{items} "
