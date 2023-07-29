from django.urls import path
from .import views


urlpatterns =[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('home',views.home,name='home'),
    path('menu',views.menu,name='menu'),
    path('gallery',views.gallery,name='gallery'),
    path('new',views.add,name='add'),
    path('reservation',views.reservation,name='reservation'),
    path('add',views.add,name='add'),
    path('check',views.check,name='check'),
    path('page',views.page,name='page'),
    path('reserv',views.reserv,name='reserv'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('additem',views.additem,name='additem'),
    path('userorderlist',views.userorderlist,name='userorderlist'),
    path('itemremove',views.itemremove,name='itemremove'),
    path('finalitems',views.finalitems,name='finalitems'),
    path('orderconfirm',views.orderconfirm,name='orderconfirm'),
    path('payment',views.payment,name='payment'),
    path('orderplace',views.orderplace,name='orderplace'),
    path('admin',views.admin,name='admin'),
    path('administrative',views.administrative,name='administrative'),
    path('checkadmin',views.checkadmin,name='checkadmin'),
    path('cancel',views.cancel,name='cancel'),
    path('admindelivered',views.admindelivered,name='admindelivered'),
    path('nindian',views.nindian,name='nindian'),
    path('chinese',views.chinese,name='chinese'),
    path('biryani',views.biryani,name='biryani'),
    path('mithai',views.mithai,name='mithai'),
    path('pizza',views.pizza,name='pizza'),
    path('desserts',views.desserts,name='desserts'),
    path('burger',views.burger,name='burger'),
    path('sindian',views.sindian,name='sindian'),
    path('myreserv',views.myreserv,name='myreserv'),
    # path('success',views.success,name='success'),






]