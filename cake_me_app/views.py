from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def splash(request):
    template = loader.get_template("splash.html")
    return HttpResponse(template.render())


def shop(request):
    template = loader.get_template("shop/shop.html")
    return HttpResponse(template.render())
