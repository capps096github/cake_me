from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def splash(request):
    template = loader.get_template("splash.html")
    return HttpResponse(template.render())


def shop(request):
    # context

    ctx = {
        "items_list": range(20),
    }
    template = loader.get_template("shop/shopx.html")

    # Render the HTML template index.html with the data in the context variable
    # return render(request, 'index.html', context=ctx)
    return HttpResponse(template.render(ctx))
