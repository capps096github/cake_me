from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.
# as per https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models#defining_the_locallibrary_models
""" Cake Model with:
- name (unique)
- price
- image_url
- description
"""

class Cake(models.Model):
    """Model representing a cake."""

    # attributes of the cake model
    # name is a CharField with a max length of 200 characters
    name = models.CharField(max_length=200, unique=True)
    # price is a DecimalField with a max_digits of 10 and a decimal_places of 2
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # image_url is a TextField without max length since it is a URL
    image_url = models.TextField()
    # description is a TextField with no max length
    description = models.TextField()

    # add ordering by name
    class Meta:
        ordering = ['name']

    # this returns the name of the cake 
    def __str__(self):
        """String for representing the Model object."""
        return f"{self.id}: {self.name} - UGX {self.price}"
    
    # get_absolute_url returns the url to access a particular instance of the model (cake) by its name
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('cake', args=[str(self.name.toLowerCase())])

""" Order Model with:
- customer_name
- customer_phone
- customer_email
- customer_address
- customer_notes
- order_date
- order_items (many to many relationship with Cake)
"""

class Order(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.CharField(max_length=50)
    customer_address = models.CharField(max_length=100)
    customer_notes = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    order_items = models.ManyToManyField(Cake)

    def __str__(self):
        return self.customer_name

""" Order Item Model with:
- order (foreign key relationship with Order)
- cake (foreign key relationship with Cake)
- quantity
"""

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.cake.name

