from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Cake


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

    # create a context dictionary
    context = {
        "cake_items": cake_items,
        "category": category,
        "title": title,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "shop/cake_shop.html", context=context)
