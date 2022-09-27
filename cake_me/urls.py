"""cake_me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add your paths to the urlpatterns list in cake_me_app/urls.py in order for them to appear
    path("cake_me/", include("cake_me_app.urls")),
    path('', RedirectView.as_view(url='cake_me/')),
    path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Use include() to add paths from the cake me application file cake_me_app/urls.py
# as per the docs here https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website
# Our site therefore renders as http://127.0.0.1:8000/cake_me/ after all the above settings are put
# It also serves the static files out of the blue with the last tag of code linking to settings.STATIC_ROOT
