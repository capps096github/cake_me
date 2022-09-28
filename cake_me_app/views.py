from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import resolve
from django.contrib.auth import login
from django.contrib.auth.models import User

from .models import Cake

from .models import Cake, Order, OrderItem

from django.contrib.auth.decorators import login_required


# Create your views here.
def splash(request):
    template = loader.get_template("splash.html")
    return HttpResponse(template.render())


@login_required
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

    # get the current user id
    user_id = request.user.id

    # get the User with the user_id from the database
    user = User.objects.get(id=user_id)

    # get the orders in the database
    orders = Order.objects.all()

    # get the order with the user if orders is not empty
    if orders:
        # get the order object by user
        order = Order.objects.get_or_create(user=user)

        # get the order items in the order if order items exist in the order
        order_items = order.order_items.all() if hasattr(order, "order_items") else None

        # get a list of all cake ids in the order via the order item
        cake_ids = [
            item.cake.id for item in order_items] if order_items else None
        # create a context dictionary add cake ids to the context dictionary if its not empty
        context = {
            "cake_items": cake_items,
            "category": category,
            "title": title,
            "cake_ids": cake_ids,
        } if cake_ids else {
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
@login_required
def add_to_cart(request, cake_id):
    # get the cake object
    cake = Cake.objects.get(id=cake_id)

    # get the current user id
    user_id = request.user.id

    # get the User with the user_id from the database
    user = User.objects.get(id=user_id)

    # get the orders in the database
    orders = Order.objects.all()

    if orders:
        # create an order object if it does not exist
        order = Order.objects.get(user=user)
    else:
        # create an order object if it does not exist
        order = Order.objects.create(user=user)

    # get the order item object if it exists else create it
    order_item, created = OrderItem.objects.get_or_create(cake_id=cake.id)

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
@login_required
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
@login_required
def remove_from_cart(request, cake_id):
    # get the cake object
    cake = Cake.objects.get(id=cake_id)

    # get the current user id
    user_id = request.user.id

    # get the User with the user_id from the database
    user = User.objects.get(id=user_id)

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
@login_required
def details(request, cake_id):
    # get the cake object
    cake = Cake.objects.get(id=cake_id)

    # get the current user id
    user_id = request.user.id

    # get the User with the user_id from the database
    user = User.objects.get(id=user_id)

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
            cake_ids = [item.cake.id for item in order_items]
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


def register(request):
    if request.method == 'POST':
        # get the username, email, password, last_name, first_name from the request
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']

        # create a new user with the username, email, and password
        user = User.objects.create_user(username, email, password)

        # set the last_name and first_name of the user
        user.last_name = last_name
        user.first_name = first_name

        # save the user
        user.save()

        # log in the user
        login(request, user)
        # redirect to the shop page
        return redirect('shop')
    else:
        return render(request, 'registration/register.html')


@login_required
def search(request):
    if request.method == 'POST':
        # get the search term from the request
        search_query = request.POST['query_text']

        # cakes_searched = Cake.objects.all().filter(name__icontains=search_query.lower() or
        # description__icontains=search_query.lower()) get the cakes in the database that match the search term by
        # name and description, price, category
        cakes_searched = Cake.objects.filter(
            Q(name__icontains=search_query.lower()) | Q(description__icontains=search_query.lower()) | Q(
                price__icontains=search_query.lower()) | Q(category__icontains=search_query.lower()))

        # count the number of cakes that match the search term
        number_of_cakes_searched = cakes_searched.count()

        context = {
            'cakes_searched': cakes_searched,
            'search_query': search_query,
            'number_of_cakes_searched': number_of_cakes_searched,
        }

        return render(request, 'search/search_cakes.html', context=context)
    else:
        return render(request, 'search/search_cakes.html')


# payment
# https://django-payments.readthedocs.io/en/latest/usage.html


# profile
@login_required
def profile(request):

    if request.method == 'POST':
        #  this gets the current user from the id and then updates their details
        # get the current user
        user = User.objects.get(id=request.user.id)

        # detect if the user is a super user
        # if user.is_superuser:

        # get the username, first_name, last_name, email, password
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']

        # set the last_name and first_name of the user
        user.username = username
        user.email = email
        user.password = password
        user.last_name = last_name
        user.first_name = first_name

        # save the user
        user.save()

        # reload the user


        # redirect to the profile page
        return redirect('profile')
        # return render(request, 'profile/profile.html')

    else:
        return render(request, 'profile/profile.html')


# check_out
def check_out(request):
    return render(request, 'check_out/check_out.html')
# cakes
def cakes(request):
    if request.method=='POST':
        cake_name=request.POST['name']
        image_url=request.POST['url']
        description=request.POST['description']
        price=request.POST['price']
        category=request.POST['category']
        

        
        Cake(name=cake_name,image_url=image_url,description=description,price=price,category=category).save()

        return redirect('shop')
    else:
        return render(request,'cakes/cakes.html')
