"""HomeDeliveryRestaurants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/',include('HomeDelivery.urls')),
    # path('admin/', admin.site.urls),
    path('menu/', include('HomeDelivery.urls')),
    path('gallery/', include('HomeDelivery.urls')),
    path('about/', include('HomeDelivery.urls')),
    path('reservation/', include('HomeDelivery.urls')),
    path('reserv/', include('HomeDelivery.urls')),
    path('home/', include('HomeDelivery.urls')),
    path('page/', include('HomeDelivery.urls')),
    path('add/', include('HomeDelivery.urls')),
    path('userlogout/', include('HomeDelivery.urls')),
    path('additem/', include('HomeDelivery.urls')),
    path('userorderlist/', include('HomeDelivery.urls')),
    path('itemremove/', include('HomeDelivery.urls')),
    path('finalitems/', include('HomeDelivery.urls')),
    path('orderconfirm/', include('HomeDelivery.urls')),
    path('payment/', include('HomeDelivery.urls')),
    path('orderplace/', include('HomeDelivery.urls')),
    path('administrative/', include('HomeDelivery.urls')),
    path('checkadmin/', include('HomeDelivery.urls')),
    path('cancel/', include('HomeDelivery.urls')),
    path('admindelivered/', include('HomeDelivery.urls')),
    path('Paratha/', include('HomeDelivery.urls')),
    path('Poori/', include('HomeDelivery.urls')),
    path('Pure_Veg/', include('HomeDelivery.urls')),
    path('Burger/', include('HomeDelivery.urls')),
    path('Noodles/', include('HomeDelivery.urls')),
    path('Pizza/', include('HomeDelivery.urls')),
    path('Gulab_Jamun/', include('HomeDelivery.urls')),
    path('Pastry/', include('HomeDelivery.urls')),
    path('myreserv/', include('HomeDelivery.urls')),
    # path('success/',include('HomeDelivery.urls')),
    path('',include('HomeDelivery.urls'))
]

