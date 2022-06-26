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


urlpatterns = [
    path('admin/',include('HomeDelivery.urls')),
    # path('admin/', admin.site.urls),
    path('menu/',include('HomeDelivery.urls')),
    path('gallery/',include('HomeDelivery.urls')),
    path('about/',include('HomeDelivery.urls')),
    path('reserv/',include('HomeDelivery.urls')),
    path('home/',include('HomeDelivery.urls')),
    path('page/',include('HomeDelivery.urls')),
    path('add/',include('HomeDelivery.urls')),
    path('userlogout/',include('HomeDelivery.urls')),
    path ('additem/',include('HomeDelivery.urls')),
    path('userorderlist/',include('HomeDelivery.urls')),
    path ('itemremove/',include('HomeDelivery.urls')),
    path('finalitems/',include('HomeDelivery.urls')),
    path('orderconfirm/',include('HomeDelivery.urls')),
    path('payment/',include('HomeDelivery.urls')),
    path('orderplace/',include('HomeDelivery.urls')),
    path('administrative/',include('HomeDelivery.urls')),
    path('checkadmin/',include('HomeDelivery.urls')),
    path('cancel/',include('HomeDelivery.urls')),
    path('admindelivered/',include('HomeDelivery.urls')),
    path('nindian/',include('HomeDelivery.urls')),
    path('chinese/',include('HomeDelivery.urls')),
    path('biryani/',include('HomeDelivery.urls')),
    path('mithai/',include('HomeDelivery.urls')),
    path('pizza/',include('HomeDelivery.urls')),
    path('desserts/',include('HomeDelivery.urls')),
    path('burger/',include('HomeDelivery.urls')),
    path('sindian/',include('HomeDelivery.urls')),
    path('myreserv/',include('HomeDelivery.urls')),
    path('',include('HomeDelivery.urls'))
]
