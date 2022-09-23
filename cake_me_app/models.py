from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
""" User Model with
- username, email, password, telephone, gender
- these fields are required and only email is unique
- they should all have helper texts
"""


class CakeMeUser(models.Model):
    # username
    username = models.CharField(max_length=50, help_text='Enter your username')
    # email
    email = models.EmailField(max_length=50, help_text='Enter your email', unique=True)
    # password
    password = models.CharField(max_length=50, help_text='Enter your password')
    # telephone
    telephone = models.CharField(max_length=20, help_text='Enter your telephone')
    # gender
    gender = models.CharField(max_length=6, help_text='Enter your Gender')

    def __str__(self):
        return f"ID: {self.id} - Username: {self.username} - Email: {self.email} - Password: {self.password} - Tel: {self.telephone} - Gender: {self.gender}"


""" Cake Model with   
- name, description, price, image_url, category
"""


class Cake(models.Model):
    # name
    name = models.CharField(max_length=50, help_text='Enter the name of the cake')
    # description
    description = models.TextField(help_text='Enter the description of the cake')
    # price
    price = models.IntegerField(help_text='Enter the price of the cake')
    # image_url
    image_url = models.TextField(help_text='Enter the image url of the cake')
    # category
    category = models.CharField(max_length=50, help_text='Enter the category of the cake', default="Sponge")

    # we want to order our cakes by name, so we need to add a class Meta
    class Meta:
        ordering = ['name']

    # we can also get a url for our cake by its name in lower case in the detail view
    def get_absolute_url(self):
        return reverse('cake_detail', args=[str(self.name).lower()])

    def __str__(self):
        return f"Name: {self.name} - Description: {self.description} - Price: {self.price} - Image: {self.image_url} - Category: {self.category}"


""" Order Model with
- userId as foreign key, total_cost, date
"""


class Order(models.Model):
    # userId
    userId = models.ForeignKey(CakeMeUser, on_delete=models.CASCADE, default="1")
    # total_cost
    total_cost = models.FloatField(help_text='Enter the total cost of the order', default=0)
    # date
    date = models.DateField(help_text='Enter the date of the order', default=timezone.now)
    # order_items list as OrderItem model many to many
    order_items = models.ManyToManyField('OrderItem')

    def __str__(self):
        return f"User: {self.userId.username} - Total Cost: {self.total_cost} - Date: {self.date}"


""" OrderItem Model with
- cake_id(foreign key), quantity, order_id(foreign key)
"""


class OrderItem(models.Model):
    # cake_id
    cake_id = models.ForeignKey(Cake, on_delete=models.CASCADE)
    # quantity
    quantity = models.IntegerField(help_text='Enter the quantity of the cake', default=0)
    # order_id
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Cake ID: {self.cake_id} - Quantity: {self.quantity} - Order ID: {self.order_id}"
