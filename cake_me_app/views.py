from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import resolve

from .models import Cake

from .models import Cake, Order, OrderItem, CakeMeUser


# Create your views here.
def splash(request):
    template = loader.get_template("splash.html")
    return HttpResponse(template.render())


def shop(request):
    # get the category query parameter from the url
    category = request.GET.get("cakes")

    # if the category is not empty
    if category == "all":
        # get all the cakes
        cake_items = Cake.objects.all()

    # if the category is all
    elif category:
        # get the cakes with the category name
        cake_items = Cake.objects.filter(category__iexact=category.lower())

    else:
        # get all the cakes
        cake_items = Cake.objects.all()

    # create a title variable from the selected category i.e all, sponge, red-velvet, butter, biscuit
    if not category or category == "all":
        title = "All"
    else:
        title = category.title()

        # check if the user is authenticated and is not null
    # if request.user.is_authenticated and request.user is not None:

    # get the CakeMeUser with an id of 1 from the database
    user = CakeMeUser.objects.get(id=1)

    # get the orders in the database
    orders = Order.objects.all()

    # get the order with the user if orders is not empty
    if orders:
        # get the order object by user
        order = Order.objects.get(user=user)

        # if the order object is not null
        if order is not None:
            # get the order items
            order_items = order.order_items.all()
            # get a list of all cake ids in the order via the order item
            cake_ids = [item.cake_id.id for item in order_items]

            # create a context dictionary add cake ids to the context dictionary if its not empty
            context = {
                "cake_items": cake_items,
                "category": category,
                "title": title,
                "cake_ids": cake_ids,
            }

        else:
            # create a context dictionary
            context = {
                "cake_items": cake_items,
                "category": category,
                "title": title,
            }
    else:
        context = {
            "cake_items": cake_items,
            "category": category,
            "title": title,
        }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "shop/cake_shop.html", context=context)


# add to cart view
def add_to_cart(request, cake_id):

    # get the cake object
    cake = Cake.objects.get(id=cake_id)

    # get the CakeMeUser with an id of 1 from the database
    user = CakeMeUser.objects.get(id=1)

    # get the orders in the database
    orders = Order.objects.all()

    if orders:
        # create an order object if it does not exist
        order = Order.objects.get(user=user)
    else:
        # create an order object if it does not exist
        order = Order.objects.create(user=user)

    # get the order item object if it exists else create it
    order_item, created = OrderItem.objects.get_or_create(cake_id=cake)

    # if it exists, update the quantity
    if not created:
        order_item.quantity += 1
        order_item.save()

    # add the order item to the order
    order.order_items.add(order_item)

    # update the order total
    order.update_total_cost()

    # save the order
    order.save()

    # if the order item has been added to cart, redirect the user back to the current page
    # return to the curent page
    return redirect(request.META.get("HTTP_REFERER"))


# update the quantity of an item in the cart
def update_quantity(request, item_id):
    # get the order item object
    order_item = OrderItem.objects.get(id=item_id)

    # get the quantity from the request
    quantity = request.POST.get("quantity")

    # update the quantity of the order item
    order_item.quantity = quantity

    # save the order item
    order_item.save()

    # if the order item has been updated, redicrect the user back to the shop page
    return redirect("details/{{item_id}}/")


# remove from cart view
def remove_from_cart(request, cake_id):
    # get the cake object
    cake = Cake.objects.get(id=cake_id)

    # get the CakeMeUser with an id of 1 from the database
    user = CakeMeUser.objects.get(id=1)

    # get the order object
    order = Order.objects.get(user=user)

    # get the order item object
    order_item = OrderItem.objects.get(cake_id=cake)

    # remove item from cart
    order.order_items.remove(order_item)

    # update the order total
    order.update_total_cost()

    # save the order
    order.save()

    # if the order item has been removed from cart, redicrect the user back to the current page
    return redirect(request.META.get("HTTP_REFERER"))


# details view
def details(request, cake_id):
    # get the cake object
    cake = Cake.objects.get(id=cake_id)

    # get the CakeMeUser with an id of 1 from the database
    user = CakeMeUser.objects.get(id=1)

    # get the orders in the database
    orders = Order.objects.all()

    # get the order with the user if orders is not empty
    if orders:
        # get the order object by user
        order = Order.objects.get(user=user)

        # if the order object is not null
        if order is not None:
            # get the order items
            order_items = order.order_items.all()
            # get a list of all cake ids in the order via the order item
            cake_ids = [item.cake_id.id for item in order_items]
            # create a context dictionary add cake ids to the context dictionary if its not empty
            context = {
                "cake": cake,
                "cake_ids": cake_ids,
            }

        else:
            # create a context dictionary
            context = {"cake": cake}
    else:
        context = {"cake": cake}

    # Render the HTML template index.html with the data in the context variable
    return render(request, "shop/details.html", context=context)



