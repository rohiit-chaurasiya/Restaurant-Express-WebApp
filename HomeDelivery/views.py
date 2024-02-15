import razorpay
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import authenticate , login,logout
from django.template import RequestContext


from HomeDeliveryRestaurants.settings import key_id, key_secret
from .models import new_user , user_orders,user_cart,orderplaceimg ,adminlogin ,adminloginpage,loginimg
from .models import item
from .models import aboutd,bottom,offers,menuitem,gallery1,reservation1,reservationb,cart,rlogo
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.conf import settings
from .models import Transaction




# client = razorpay.Client(auth=(key_id,key_secret))
# Create your views here.
# razorpay_client = razorpay.Client(auth=(settings.key_id, settings.key_secret))


usercheck=False
def check(request):
    global otherpage , usercheck,imglogin
    sliders = [slider1, slider2, slider3]
    items = [item1, item2, item3, item4, item5, item6, item7, item8, item9]
    items2 = [item10, item11, item12, item13, item14, item15, item16, item17, item18]
    features = [feature1, feature2, feature3]
    chefs = [chef1, chef2, chef3, chef4]
    webd = [awebd]
    webds = [webd1, webd2]
    if request.method == 'POST':
        fpassword1 = request.POST['pass1']
        fusername = request.POST['username']
        if new_user.objects.filter(username=fusername).exists() and new_user.objects.filter(pass1=fpassword1).exists():
            usercheck=True
            otherpage = fusername
            print("success1")
            return render(request, 'index.html',{'sliders': sliders, 'fmenu': fmenu, 'smenu': smenu, 'mitem1': mitem1, 'mitem2': mitem2,
                           'items': items, 'items2': items2, 'features': features, 'chefs': chefs, 'location': location,'time': time, 'reserv': reserv,
                           'webds': webds, 'webd': webd, 'off': off, 'otherpage': otherpage,'logor':logor})
        else:
            print("success2")
            return render(request, 'login.html', {'webd': webd, 'webds': webds,'imglogin':imglogin,'logor':logor})
    else:
        print("worng")
        return render(request, 'login.html', {'webd': webd, 'webds': webds,'imglogin':imglogin,'logor':logor})


def index(request):
    global imglogin
    imglogin = loginimg()
    imglogin.img = 'about1.jpg'
    #cart-------------------------
    global logor
    logor=rlogo()
    logor.img='RE.png'

    # ------------------------------------
    global ucart
    ucart = cart()
    ucart.img = 'cart.png'
    #features-----------------------------
    global feature1
    feature1=item()
    feature1.name='BEAUTIFUL LOCATION.'
    feature1.img='det/1.jpg'
    feature1.det='FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'

    global feature2
    feature2 = item()
    feature2.name = 'FEEL THE TASTE.'
    feature2.img = 'det/2.jpg'
    feature2.det = 'NOTHING BRINGS PEOPLE TOGETHER LIKE GOOD FOOD.'

    global feature3
    feature3=item()
    feature3.name='DELICIOUS DESSERTS.'
    feature3.img='det/3.jpg'
    feature3.det='THE BEST THINGS IN LIFE ARE SWEET.'



    #slider-------------------------------------------------------------
    global slider1,slider2,slider3,sliders
    slider1=item()
    slider1.img='slider/nss2.jpg'
    slider2=item()
    slider2.img='slider/test1.jpg'
    slider3=item()
    slider3.img='slider/test3.jpg'

    #meni items-----------------------------------------------------------
    global fmenu,mitem1,mitem2,smenu
    fmenu=item()
    fmenu.img='menu/menub.jpg'
    smenu=item()
    smenu.img='menu/menua.jpg'


    mitem1=item()
    mitem1.name='Breakfast burrito'
    mitem1.img='menu/breakfast/1.jpg'
    mitem1.det='It is veery testy'
    mitem1.price='60'

    mitem2 = item()
    mitem2.name = 'Omlet'
    mitem2.img = 'menu/breakfast/2.jpg'
    mitem2.det = 'It is veery testy'
    mitem2.price = '70'

    #item list- -----------------------------------------------------------1
    global item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,item18
    item1 = item()
    item1.name = 'Breakfast burrito'
    item1.img = 'menu/breakfast/1.jpg'
    item1.price = '80'

    item2 = item()
    item2.name = 'Omlet'
    item2.img = 'menu/breakfast/2.jpg'
    item2.price = '75'

    item3 = item()
    item3.name = 'Cheese'
    item3.img = 'menu/breakfast/3.jpg'
    item3.price = '45'

    item4 = item()
    item4.name = 'Milk'
    item4.img = 'menu/breakfast/4.jpg'
    item4.price = '54'

    item5 = item()
    item5.name = 'Pizza'
    item5.img = 'menu/breakfast/5.jpg'
    item5.price = '70'

    item6 = item()
    item6.name = 'Double Omlet'
    item6.img = 'menu/breakfast/6.jpg'
    item6.price = '120'

    item7 = item()
    item7.name = 'hamburger'
    item7.img = 'menu/breakfast/7.jpg'
    item7.price = '50'

    item8= item()
    item8.name = 'Cake'
    item8.img = 'menu/breakfast/8.jpg'
    item8.price = '85'

    item9 = item()
    item9.name = 'Velvet Cake'
    item9.img = 'menu/desserts/1.jpg'
    item9.price = '95'

    # item list-------------------------------------------------2
    item10 = item()
    item10.name = 'Chocolate Cake'
    item10.img = 'menu/desserts/2.jpg'
    item10.price = '95'

    item11 = item()
    item11.name = 'Cream Cake'
    item11.img = 'menu/desserts/3.jpg'
    item11.price = '70'

    item12 = item()
    item12.name = 'Sol Cake'
    item12.img = 'menu/desserts/4.jpg'
    item12.price = '35'

    item13 = item()
    item13.name = 'Sol Cake '
    item13.img = 'menu/desserts/5.jpg'
    item13.price = '45'

    item14 = item()
    item14.name = 'Truffle Cake'
    item14.img = 'menu/desserts/6.jpg'
    item14.price = '45'

    item15 = item()
    item15.name = 'Forest Cake '
    item15.img = 'menu/desserts/7.jpg'
    item15.price = '55'

    item16 = item()
    item16.name = 'Pineapple cake'
    item16.img = 'menu/desserts/8.jpg'
    item16.price = '65'

    item17 = item()
    item17.name = 'Papper Pizza'
    item17.img = 'menu/pizza/1.jpg'
    item17.price = '175'

    item18 = item()
    item18.name = 'Meatza Pizz'
    item18.img = 'menu/pizza/2.jpg'
    item18.price = '285'

    #chefs-----------------------------------------------------
    global chef1,chef2,chef3,chef4,chefs
    chef1=item()
    chef1.name='Vicky Ratnani'
    chef1.img='chef/chef4.jpg'
    chef1.det='Indian'
    chef1.skill1='Fish'
    chef1.skill2='Shrimp'
    chef1.skill3 = 'Salad'
    chef1.skill4= 'Sandwich'
    chef1.skill5='Bread'

    chef2 = item()
    chef2.name = 'Romy Gill'
    chef2.img = 'chef/chef1.jpg'
    chef2.det = 'Indian'
    chef2.skill1 = 'Rice'
    chef2.skill2 = 'Spaghetti'
    chef2.skill3 = 'Pizza'
    chef2.skill4 = 'Hamburger'
    chef2.skill5 = 'Eggs'

    chef3=item()
    chef3.name='Sanjeev kumar'
    chef3.img='chef/chef3.jpg'
    chef3.det='indian'
    chef3.skill1 = 'Cheese'
    chef3.skill2 = 'Sausages'
    chef3.skill3 = 'Candy'
    chef3.skill4 = 'Tea'
    chef3.skill5 = 'Cookie'

    chef4=item()
    chef4.name='Vineet Bhatia'
    chef4.img='chef/chef2.jpg'
    chef4.det='Indian'
    chef4.skill1 = 'Cake'
    chef4.skill2 = 'Pie'
    chef4.skill3 = 'Cupcake'
    chef4.skill4 = 'Sweet'
    chef4.skill5 = 'Bitter'

    global location
    location=item()
    location.name='KIET Group of Institutions'
    location.det='Ghaziabad,206201'

    global time
    time=item()
    time.det='SUN - THU | 07:00 - 23:00'
    time.name='FRI - SAT | 08:00 - 01:00'

    global reserv
    reserv=item()
    reserv.name='MOBILE: +91-8840854918'
    reserv.det='E-MAIL: rohiit.chaurasiya@gmail.com'

    global awebd
    awebd = bottom()
    awebd.name = 'Aayushmaan Restaurant'
    awebd.img1 = 'menu/footer.jpg'
    awebd.img2 = 'headertop.png'
    awebd.det = 'Aayushmaan Community © 2023'

    global webd1
    webd1 = bottom()
    webd1.name = 'Offers'
    webd1.op1 = '50% off'
    webd1.op2 = '40% off'
    webd1.op3 = '60% off'
    webd1.op4 = '10% Cashback'
    webd1.op5 = 'Free Delivery'

    global webd2
    webd2 = bottom()
    webd2.name = 'Staff'
    webd2.op1 = 'Chif'
    webd2.op2 = 'Staff'
    webd2.op3 = 'Baker'
    webd2.op4 = 'Counter Server'
    webd2.op5 = 'Bus Person'


    #--------------------------------------------Offers ------------------------------------
    global off
    off=offers()
    off.name='Offers'
    off.det='60% off upto Rs.120 | Use Coupon WELCOME '

#=================================================================================================================================
    sliders=[slider1,slider2,slider3]
    items=[item1,item2,item3,item4,item5,item6,item7,item8,item9]
    items2=[item10,item11,item12,item13,item14,item15,item16,item17,item18]
    features=[feature1,feature2,feature3]
    chefs=[chef1,chef2,chef3,chef4]
    global webds
    webds=[webd1,webd2]
    webd=[awebd]
    return render(request,'index.html', {'sliders':sliders,'fmenu':fmenu,'smenu':smenu,'mitem1':mitem1,'mitem2':mitem2,'items':items,'items2':items2,
    'features':features,'chefs':chefs,'location':location,'time':time,'reserv':reserv,'webds':webds,'webd':webd,'off':off,'logor':logor})


def home(request):
    sliders = [slider1, slider2, slider3]
    items = [item1, item2, item3, item4, item5, item6, item7, item8, item9]
    items2 = [item10, item11, item12, item13, item14, item15, item16, item17, item18]
    features = [feature1, feature2, feature3]
    chefs = [chef1, chef2, chef3, chef4]
    webds = [webd1, webd2]
    webd = [awebd]
    print("home")
    global otherpage
    check(request)
    if usercheck == True:
        print("if")
        print(otherpage)
        return render(request, 'index.html',
                      {'sliders': sliders, 'fmenu': fmenu, 'smenu': smenu, 'mitem1': mitem1, 'mitem2': mitem2,
                       'items': items, 'items2': items2,
                       'features': features, 'chefs': chefs, 'location': location, 'time': time, 'reserv': reserv,
                       'webds': webds, 'webd': webd, 'off': off,'otherpage':otherpage,'logor':logor})
    else:
        print("else")
        return render(request, 'index.html',
                      {'sliders': sliders, 'fmenu': fmenu, 'smenu': smenu, 'mitem1': mitem1, 'mitem2': mitem2,
                       'items': items, 'items2': items2,
                       'features': features, 'chefs': chefs, 'location': location, 'time': time, 'reserv': reserv,
                       'webds': webds, 'webd': webd, 'off': off,'logor':logor})


def about(request):
    # =====================about
    aboutr = aboutd()
    aboutr.name = 'Restaurant Express'
    aboutr.img = 'about1.jpg'
    aboutr.det = 'The Right Ingredients for the Right Food.'
    aboutr.desc = 'Location: Ghaziabad'

    chefs = [chef1, chef2, chef3, chef4]
    webd=[awebd]
    webds=[webd1,webd2]
    check(request)
    if usercheck == True:
        print("if")
        print(otherpage)
        return render(request,'about.html',{'aboutr':aboutr,'webds':webds,'webd':webd,'chefs':chefs,'otherpage':otherpage,'logor':logor})
    else:
        return render(request, 'about.html', {'aboutr':aboutr,'webds': webds, 'webd': webd, 'chefs': chefs,'logor':logor})


def menu(request):
    global otherpage, menuslider
    check(request)

    offer= offers()
    offer.name='Get 50% off on Your First Order'

    menuslider=menuitem()
    menuslider.img='menu6.jpg'

    menu1=menuitem()
    menu1.name='Paneer Delight'
    menu1.img='menu/salad/1.jpg'
    menu1.det=' TASTE BETTER.'
    menu1.price='200'

    menu2 = menuitem()
    menu2.name = 'Paneer Salad'
    menu2.img = 'menu/salad/2.jpg'
    menu2.det = 'TASTE BETTER'
    menu2.price = '470'

    menu3 = menuitem()
    menu3.name = 'Tofu Salad'
    menu3.img = 'menu/salad/3.jpg'
    menu3.det = ' TASTES BETTER'
    menu3.price = '265'

    menu4 = menuitem()
    menu4.name = 'Mashroom Salad'
    menu4.img = 'menu/salad/4.jpg'
    menu4.det = 'SALAD'
    menu4.price = '370'

    menu5 = menuitem()
    menu5.name = 'Masala Salad'
    menu5.img = 'menu/salad/5.jpg'
    menu5.det = 'SALAD'
    menu5.price = '450'

    menu6 = menuitem()
    menu6.name = 'Chicken salad'
    menu6.img = 'menu/salad/6.jpg'
    menu6.det = 'SALAD'
    menu6.price = '200'

    menu7 = menuitem()
    menu7.name = 'Buster Mushroom Salad '
    menu7.img = 'menu/salad/7.jpg'
    menu7.det = 'SALAD'
    menu7.price = '200'

    menu8 = menuitem()
    menu8.name = 'Mango Salad'
    menu8.img = 'menu/salad/8.jpg'
    menu8.det = 'SALAD'
    menu8.price = '200'

    menu9 = menuitem()
    menu9.name = 'Margherita'
    menu9.img = 'menu/pizza/1.jpg'
    menu9.det = 'PIZZA'
    menu9.price = '200'

    menu10 = menuitem()
    menu10.name = 'Double Cheese pizza'
    menu10.img = 'menu/pizza/2.jpg'
    menu10.det = 'PIZZA'
    menu10.price = '200'

    menu11= menuitem()
    menu11.name = 'Veggle feast'
    menu11.img = 'menu/pizza/3.jpg'
    menu11.det = 'PIZZA'
    menu11.price = '200'

    menu12 = menuitem()
    menu12.name = 'Special Paneer'
    menu12.img = 'menu/pizza/4.jpg'
    menu12.det = 'PIZZA'
    menu12.price = '200'

    menu13 = menuitem()
    menu13.name = 'Supreme'
    menu13.img = 'menu/pizza/5.jpg'
    menu13.det = 'PIZZA'
    menu13.price = '200'

    menu14 = menuitem()
    menu14.name = 'Primo Meats'
    menu14.img = 'menu/pizza/6.jpg'
    menu14.det = 'PIZZA'
    menu14.price = '200'

    menu15 = menuitem()
    menu15.name = 'Chicken Tikka'
    menu15.img = 'menu/pizza/7.jpg'
    menu15.det = 'PIZZA'
    menu15.price = '200'

    menu16 = menuitem()
    menu16.name = 'Keema Masala'
    menu16.img = 'menu/pizza/8.jpg'
    menu16.det = 'PIZZA'
    menu16.price = '200'



    menu27= menuitem()
    menu27.name = 'Waffles'
    menu27.img = 'menu/breakfast/3.jpg'
    menu27.det = 'BREAKFAST'
    menu27.price = '200'

    menu28 = menuitem()
    menu28.name = 'Milk'
    menu28.img = 'menu/breakfast/4.jpg'
    menu28.det = 'BREAKFAST'
    menu28.price = '200'

    menu29 = menuitem()
    menu29.name = 'Pizza'
    menu29.img = 'menu/breakfast/5.jpg'
    menu29.det = 'BREAKFAST'
    menu29.price = '200'

    menu30 = menuitem()
    menu30.name = 'Eggs'
    menu30.img = 'menu/breakfast/6.jpg'
    menu30.det = 'BREAKFAST'
    menu30.price = '200'

    menu31 = menuitem()
    menu31.name = 'Sandwich'
    menu31.img = 'menu/breakfast/7.jpg'
    menu31.det = 'BREAKFAST'
    menu31.price = '200'

    menu32 = menuitem()
    menu32.name = 'Cake'
    menu32.img = 'menu/breakfast/8.jpg'
    menu32.det = 'BREAKFAST'
    menu32.price = '200'

    menu33 = menuitem()
    menu33.name = 'Buster Mushroom Salad '
    menu33.img = 'menu/salad/7.jpg'
    menu33.det = 'SALAD'
    menu33.price = '200'

    menu34 = menuitem()
    menu34.name = 'Mango Salad'
    menu34.img = 'menu/salad/8.jpg'
    menu34.det = 'SALAD'
    menu34.price = '200'

    menu35= menuitem()
    menu35.name = 'Margherita'
    menu35.img = 'menu/pizza/1.jpg'
    menu35.det = 'PIZZA'
    menu35.price = '2'

    menu36 = menuitem()
    menu36.name = 'Double Cheese pizza'
    menu36.img = 'menu/pizza/2.jpg'
    menu36.det = 'PIZZA'
    menu36.price = '200'



    menus=[menu1,menu2,menu3,menu4,menu5,menu6,menu7,menu8,menu9,menu10,menu11,menu12,menu13,menu14,menu15,menu16,menu27,menu28,menu29,menu30,menu31,menu32,menu33,menu34,menu35,menu36]
    webd = [awebd]
    webds = [webd1, webd2]
    if usercheck == True:
        print("if")
        print(otherpage)
        return render(request,'menu.html',{'menus':menus,'offer':offer,'webd':webd,'webds':webds,'otherpage':otherpage,'logor':logor,'menuslider':menuslider})
    else:
        return render(request, 'menu.html', {'menus': menus, 'offer': offer, 'webd': webd, 'webds': webds,'logor':logor,'menuslider':menuslider})

def Paratha(request):

    global otherpage,listname
    check(request)
    listname="Paratha"

    offer= offers()
    offer.name='Get 50% off on Your First Order'

    menu1=menuitem()
    menu1.name='Aloo Onion Paratha'
    menu1.img='menu/paratha/1.jpg'
    menu1.det='FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu1.price='200'

    menu2 = menuitem()
    menu2.name = 'Veg Kima Paratha'
    menu2.img = 'menu/paratha/2.jpg'
    menu2.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu2.price = '470'

    menu3 = menuitem()
    menu3.name = 'Chilli Onion Paratha'
    menu3.img = 'menu/paratha/3.jpg'
    menu3.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu3.price = '265'

    menu4 = menuitem()
    menu4.name = 'Plan Paratha '
    menu4.img = 'menu/paratha/4.jpg'
    menu4.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu4.price = '370'

    menu5 = menuitem()
    menu5.name = 'Ajwan Paratha'
    menu5.img = 'menu/paratha/5.jpg'
    menu5.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu5.price = '450'

    menu6 = menuitem()
    menu6.name = 'Onion Masala Paratha'
    menu6.img = 'menu/paratha/6.jpg'
    menu6.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu6.price = '200'

    menu7 = menuitem()
    menu7.name = 'Kima Onion Paratha'
    menu7.img = 'menu/paratha/7.jpg'
    menu7.det = 'd'
    menu7.price = '200'



    menus=[menu1,menu2,menu3,menu4,menu5,menu6,menu7]
    webd = [awebd]
    webds = [webd1, webd2]
    if usercheck == True:
        print("if")
        print(otherpage)
        return render(request,'menu.html',{'menus':menus,'offer':offer,'webd':webd,'webds':webds,'otherpage':otherpage,'listname':listname,'logor':logor,'menuslider':menuslider})
    else:
        return render(request, 'menu.html', {'menus': menus, 'offer': offer, 'webd': webd, 'webds': webds,'listname':listname,'logor':logor,'menuslider':menuslider})

def Poori(request):

    global otherpage ,listname
    check(request)
    listname="Poori"

    offer= offers()
    offer.name='Get 50% off on Your First Order'

    menu1=menuitem()
    menu1.name='Puffy Poori'
    menu1.img='menu/poori/1.avif'
    menu1.det='FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu1.price='200'

    menu2 = menuitem()
    menu2.name = 'Chola Poori'
    menu2.img = 'menu/poori/2.avif'
    menu2.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu2.price = '470'

    menu3 = menuitem()
    menu3.name = 'Aloo Puri'
    menu3.img = 'menu/poori/3.avif'
    menu3.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu3.price = '265'

    menu4 = menuitem()
    menu4.name = 'Paneer Poori'
    menu4.img = 'menu/poori/4.avif'
    menu4.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu4.price = '370'

    menu5 = menuitem()
    menu5.name = 'Ragi Poori'
    menu5.img = 'menu/poori/5.avif'
    menu5.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu5.price = '450'

    menu6 = menuitem()
    menu6.name = 'Palak Poori'
    menu6.img = 'menu/poori/6.avif'
    menu6.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu6.price = '200'

    menu7 = menuitem()
    menu7.name = 'Beetroot Poori'
    menu7.img = 'menu/poori/7.avif'
    menu7.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu7.price = '200'

    menu8 = menuitem()
    menu8.name = 'Kuttu Poori'
    menu8.img = 'menu/poori/8.avif'
    menu8.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu8.price = '200'



    menus=[menu1,menu2,menu3,menu4,menu5,menu6,menu7,menu8]
    webd = [awebd]
    webds = [webd1, webd2]
    if usercheck == True:
        print("if")
        print(otherpage)
        return render(request,'menu.html',{'menus':menus,'offer':offer,'webd':webd,'webds':webds,'otherpage':otherpage,'listname':listname,'logor':logor,'menuslider':menuslider})
    else:
        return render(request, 'menu.html', {'menus': menus, 'offer': offer, 'webd': webd, 'webds': webds,'listname':listname,'logor':logor,'menuslider':menuslider})

def Pure_Veg(request):

    global otherpage,listname
    check(request)
    listname="Pure_Veg"

    offer= offers()
    offer.name='Get 50% off on Your First Order'

    menu1=menuitem()
    menu1.name='Masala Channa'
    menu1.img='menu/pure_veg/1.avif'
    menu1.det='FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu1.price='200'

    menu2 = menuitem()
    menu2.name = 'Protein-Packed Diet'
    menu2.img = 'menu/pure_veg/2.avif'
    menu2.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu2.price = '470'

    menu3 = menuitem()
    menu3.name = ' Pommes Gratin'
    menu3.img = 'menu/pure_veg/3.avif'
    menu3.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu3.price = '265'

    menu4 = menuitem()
    menu4.name = 'Vegetarian Burritos'
    menu4.img = 'menu/pure_veg/4.avif'
    menu4.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu4.price = '370'

    menu5 = menuitem()
    menu5.name = 'Vegetarian Nargisi Kofta'
    menu5.img = 'menu/pure_veg/5.avif'
    menu5.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu5.price = '450'

    menu6 = menuitem()
    menu6.name = ' Paneer Kali Mirch'
    menu6.img = 'menu/pure_veg/6.avif'
    menu6.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu6.price = '200'

    menu7 = menuitem()
    menu7.name = 'Vegetarian Khow Suey'
    menu7.img = 'menu/pure_veg/7.avif'
    menu7.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu7.price = '200'

    menu8 = menuitem()
    menu8.name = 'Matar Ka Dulma'
    menu8.img = 'menu/pure_veg/8.avif'
    menu8.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu8.price = '200'

    menu9 = menuitem()
    menu9.name = 'Vegetable Lasagne '
    menu9.img = 'menu/pure_veg/9.avif'
    menu9.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu9.price = '200'


    menus=[menu1,menu2,menu3,menu4,menu5,menu6,menu7,menu8,menu9]
    webd = [awebd]
    webds = [webd1, webd2]
    if usercheck == True:
        print("if")
        print(otherpage)
        return render(request,'menu.html',{'menus':menus,'offer':offer,'webd':webd,'webds':webds,'otherpage':otherpage,'listname':listname,'logor':logor,'menuslider':menuslider})
    else:
        return render(request, 'menu.html', {'menus': menus, 'offer': offer, 'webd': webd, 'webds': webds,'listname':listname,'logor':logor,'menuslider':menuslider})

def Burger(request):

    global otherpage,listname
    check(request)
    listname="Burger"

    offer= offers()
    offer.name='Get 50% off on Your First Order'

    menu1=menuitem()
    menu1.name='Aloo Tikki Burger'
    menu1.img='menu/burger/1.avif'
    menu1.det='FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu1.price='200'

    menu2 = menuitem()
    menu2.name = 'Paneer Masala Burger'
    menu2.img = 'menu/burger/2.avif'
    menu2.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu2.price = '470'

    menu3 = menuitem()
    menu3.name = 'Chicken Seekh Burger'
    menu3.img = 'menu/burger/2.avif'
    menu3.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu3.price = '265'

    menu4 = menuitem()
    menu4.name = 'Tandoori Tikka Burger'
    menu4.img = 'menu/burger/3.avif'
    menu4.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu4.price = '370'

    menu5 = menuitem()
    menu5.name = 'Chana Chaat Burger'
    menu5.img = 'menu/burger/4.avif'
    menu5.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu5.price = '450'

    menu6 = menuitem()
    menu6.name = 'Butter Chicken Burger'
    menu6.img = 'menu/burger/5.avif'
    menu6.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu6.price = '200'

    menu7 = menuitem()
    menu7.name = 'Masala Vada Burger'
    menu7.img = 'menu/burger/6.avif'
    menu7.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu7.price = '200'

    menu8 = menuitem()
    menu8.name = 'Chole Bhature Burger'
    menu8.img = 'menu/burger/7.avif'
    menu8.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu8.price = '200'

    menu9 = menuitem()
    menu9.name = 'Veggie Kebab Burger'
    menu9.img = 'menu/burger/8.avif'
    menu9.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu9.price = '200'

    menu10 = menuitem()
    menu10.name = 'Butter Masala Burger'
    menu10.img = 'menu/burger/9.avif'
    menu10.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu10.price = '200'

    menu11= menuitem()
    menu11.name = 'Pav Bhaji Burger'
    menu11.img = 'menu/burger/10.avif'
    menu11.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu11.price = '200'

    menu12 = menuitem()
    menu12.name = 'Malai Kofta Burger'
    menu12.img = 'menu/burger/11.avif'
    menu12.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu12.price = '200'

    menu13 = menuitem()
    menu13.name = 'Palak Paneer Burger'
    menu13.img = 'menu/burger/12.avif'
    menu13.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu13.price = '200'

    menu14 = menuitem()
    menu14.name = 'Keema Pav Burger'
    menu14.img = 'menu/burger/13.avif'
    menu14.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu14.price = '200'

    menu15 = menuitem()
    menu15.name = 'Achari Chicken Burger'
    menu15.img = 'menu/burger/14.avif'
    menu15.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu15.price = '200'

    menu16 = menuitem()
    menu16.name = 'Rajma Galouti Burger'
    menu16.img = 'menu/burger/15.avif'
    menu16.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu16.price = '200'

    menu17 = menuitem()
    menu17.name = 'Pani Puri Burger'
    menu17.img = 'menu/burger/16.avif'
    menu17.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu17.price = '200'

    menu18 = menuitem()
    menu18.name = 'Masala Omelette Burger'
    menu18.img = 'menu/burger/17.avif'
    menu18.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu18.price = '200'

    menu19 = menuitem()
    menu19.name = 'Samosa Chaat Burger'
    menu19.img = 'menu/burger/18.avif'
    menu19.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu19.price = '200'

    menu20 = menuitem()
    menu20.name = 'Mutton Biryani Burger'
    menu20.img = 'menu/burger/19.avif'
    menu20.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu20.price = '200'

    menu21 = menuitem()
    menu21.name = 'Vada Pav Burger'
    menu21.img = 'menu/burger/20.avif'
    menu21.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu21.price = '200'

    menu22 = menuitem()
    menu22.name = 'Kaju Paneer Burger'
    menu22.img = 'menu/burger/21.avif'
    menu22.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu22.price = '200'

    menu23 = menuitem()
    menu23.name = 'Fish Amritsari Burger'
    menu23.img = 'menu/burger/22.avif'
    menu23.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu23.price = '200'

    menu24 = menuitem()
    menu24.name = 'Manchurian Burger'
    menu24.img = 'menu/burger/23.avif'
    menu24.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu24.price = '200'

    menu25 = menuitem()
    menu25.name = 'Mushroom Burger'
    menu25.img = 'menu/burger/25.avif'
    menu25.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu25.price = '200'

    menu26= menuitem()
    menu26.name = 'Pudina Chicken Burger'
    menu26.img = 'menu/burger/26.avif'
    menu26.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu26.price = '200'

    menu27= menuitem()
    menu27.name = 'Tikka Masala Burger'
    menu27.img = 'menu/burger/27.avif'
    menu27.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu27.price = '200'

    menu28 = menuitem()
    menu28.name = 'Methi Thepla Burger'
    menu28.img = 'menu/burger/28.avif'
    menu28.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu28.price = '200'

    menu29 = menuitem()
    menu29.name = 'Chettinad Chicken Burger'
    menu29.img = 'menu/burger/29.avif'
    menu29.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu29.price = '200'

    menu30 = menuitem()
    menu30.name = 'Chai-Spiced Burger'
    menu30.img = 'menu/burger/30.jpg'
    menu30.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu30.price = '200'

    menu31 = menuitem()
    menu31.name = 'Rasgulla Dessert Burger'
    menu31.img = 'menu/burger/31.jpg'
    menu31.det = 'INDULGE IN FLAVORS THAT PAINT JOY ON YOUR TASTE BUDS.'
    menu31.price = '200'


    menus=[menu1,menu2,menu3,menu4,menu5,menu6,menu7,menu8,menu9,menu10,menu11,menu12,menu13,menu14,menu15,menu16,menu17,menu18,menu19,menu20,
           menu21,menu22,menu23,menu24,menu25,menu26,menu27,menu28,menu29,menu30,menu31]
    webd = [awebd]
    webds = [webd1, webd2]
    if usercheck == True:
        print("if")
        print(otherpage)
        return render(request,'menu.html',{'menus':menus,'offer':offer,'webd':webd,'webds':webds,'otherpage':otherpage,'listname':listname,'logor':logor,'menuslider':menuslider})
    else:
        return render(request, 'menu.html', {'menus': menus, 'offer': offer, 'webd': webd, 'webds': webds,'listname':listname,'logor':logor,'menuslider':menuslider})

def Noodles(request):

    global otherpage,listname
    check(request)
    listname='Noodles'

    offer= offers()
    offer.name='Get 50% off on Your First Order'

    menu1=menuitem()
    menu1.name='Chana Noodle'
    menu1.img='menu/noodles/1.avif'
    menu1.det='FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu1.price='200'

    menu2 = menuitem()
    menu2.name = 'Hakka Noodle'
    menu2.img = 'menu/noodles/2.avif'
    menu2.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu2.price = '470'

    menu3 = menuitem()
    menu3.name = 'Vermicelli Upma Noodle'
    menu3.img = 'menu/noodles/3.avif'
    menu3.det = 'Elevate your senses with every delectable bite.'
    menu3.price = '265'

    menu4 = menuitem()
    menu4.name = 'Poha Noodles'
    menu4.img = 'menu/noodles/4.avif'
    menu4.det = 'Elevate your senses with every delectable bite.'
    menu4.price = '370'

    menu5 = menuitem()
    menu5.name = 'Sevai Noodles'
    menu5.img = 'menu/noodles/5.avif'
    menu5.det = 'Elevate your senses with every delectable bite.'
    menu5.price = '450'

    menu6 = menuitem()
    menu6.name = 'Jalebi Noodle'
    menu6.img = 'menu/noodles/6.avif'
    menu6.det = 'Elevate your senses with every delectable bite.'
    menu6.price = '200'

    menu7 = menuitem()
    menu7.name = 'Khar Puli Noodle'
    menu7.img = 'menu/noodles/7.avif'
    menu7.det = 'Elevate your senses with every delectable bite.'
    menu7.price = '200'

    menu8 = menuitem()
    menu8.name = 'Thukpa Noodle'
    menu8.img = 'menu/noodles/8.avif'
    menu8.det = 'Elevate your senses with every delectable bite.'
    menu8.price = '200'

    menu9 = menuitem()
    menu9.name = 'Lukhmi Noodle'
    menu9.img = 'menu/noodles/9.avif'
    menu9.det = 'Elevate your senses with every delectable bite.'
    menu9.price = '200'

    menu10 = menuitem()
    menu10.name = 'Sheer Khurma Noodle'
    menu10.img = 'menu/noodles/10.avif'
    menu10.det = 'Elevate your senses with every delectable bite.'
    menu10.price = '200'

    menu11= menuitem()
    menu11.name = 'Coca Noodle'
    menu11.img = 'menu/noodles/11.avif'
    menu11.det = 'Elevate your senses with every delectable bite.'
    menu11.price = '200'

    menu12 = menuitem()
    menu12.name = 'Instant Noodle'
    menu12.img = 'menu/noodles/12.avif'
    menu12.det = 'Elevate your senses with every delectable bite.'
    menu12.price = '200'

    menu13 = menuitem()
    menu13.name = 'Frozen Noodle'
    menu13.img = 'menu/noodles/13.avif'
    menu13.det = 'Elevate your senses with every delectable bite.'
    menu13.price = '200'

    menu14 = menuitem()
    menu14.name = 'Cup Noodle'
    menu14.img = 'menu/noodles/14.avif'
    menu14.det = 'Elevate your senses with every delectable bite.'
    menu14.price = '200'


    menus=[menu1,menu2,menu3,menu4,menu5,menu6,menu7,menu8,menu9,menu10,menu11,menu12,menu13,menu14]
    webd = [awebd]
    webds = [webd1, webd2]
    if usercheck == True:
        print("if")
        print(otherpage)
        return render(request,'menu.html',{'menus':menus,'offer':offer,'webd':webd,'webds':webds,'otherpage':otherpage,'listname':listname,'logor':logor,'menuslider':menuslider})
    else:
        return render(request, 'menu.html', {'menus': menus, 'offer': offer, 'webd': webd, 'webds': webds,'listname':listname,'logor':logor,'menuslider':menuslider})

def Pizza(request):

    global otherpage,listname
    check(request)
    listname='Pizza'

    offer= offers()
    offer.name='Get 50% off on Your First Order'

    menu1=menuitem()
    menu1.name='Tandoori Tikka Pizza'
    menu1.img='menu/pizza/1.jpg'
    menu1.det='FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu1.price='200'

    menu2 = menuitem()
    menu2.name = 'Paneer Makhani Pizza'
    menu2.img = 'menu/pizza/2.jpg'
    menu2.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu2.price = '470'

    menu3 = menuitem()
    menu3.name = 'Butter Chicken Pizza'
    menu3.img = 'menu/pizza/3.jpg'
    menu3.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu3.price = '265'

    menu4 = menuitem()
    menu4.name = 'Mumbai Masala Pizza'
    menu4.img = 'menu/pizza/4.jpg'
    menu4.det = "IN EVERY RECIPE, THERE'S A STORY WAITING TO BE SAVORED."
    menu4.price = '370'

    menu5 = menuitem()
    menu5.name = 'Spicy Vada Pizzetta'
    menu5.img = 'menu/pizza/5.jpg'
    menu5.det = "IN EVERY RECIPE, THERE'S A STORY WAITING TO BE SAVORED."
    menu5.price = '450'

    menu6 = menuitem()
    menu6.name = 'Chaat Crunch Pizza'
    menu6.img = 'menu/pizza/6.jpg'
    menu6.det = "IN EVERY RECIPE, THERE'S A STORY WAITING TO BE SAVORED."
    menu6.price = '200'

    menu7 = menuitem()
    menu7.name = 'Palak Paneer Pizza'
    menu7.img = 'menu/pizza/7.jpg'
    menu7.det = "IN EVERY RECIPE, THERE'S A STORY WAITING TO BE SAVORED."
    menu7.price = '200'

    menu8 = menuitem()
    menu8.name = 'Coconut Curry Pizza'
    menu8.img = 'menu/pizza/8.jpg'
    menu8.det = "IN EVERY RECIPE, THERE'S A STORY WAITING TO BE SAVORED."
    menu8.price = '200'



    menus=[menu1,menu2,menu3,menu4,menu5,menu6,menu7,menu8]
    webd = [awebd]
    webds = [webd1, webd2]
    if usercheck == True:
        print("if")
        print(otherpage)
        return render(request,'menu.html',{'menus':menus,'offer':offer,'webd':webd,'webds':webds,'otherpage':otherpage,'listname':listname,'logor':logor,'menuslider':menuslider})
    else:
        return render(request, 'menu.html', {'menus': menus, 'offer': offer, 'webd': webd, 'webds': webds,'listname':listname,'logor':logor,'menuslider':menuslider})

def Gulab_Jamun(request):

    global otherpage,listname
    check(request)
    listname="Gulab_Jamun"

    offer= offers()
    offer.name='Get 50% off on Your First Order'

    menu1=menuitem()
    menu1.name='Kala Jamun'
    menu1.img='menu/gulab_jamun/1.avif'
    menu1.det='LIFE IS SWEETER WITH A SPRINKLE OF INDULGENCE.'
    menu1.price='200'

    menu2 = menuitem()
    menu2.name = 'Dry Gulab Jamun'
    menu2.img = 'menu/gulab_jamun/8.avif'
    menu2.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu2.price = '470'

    menu3 = menuitem()
    menu3.name = 'Kesari Gulab Jamun'
    menu3.img = 'menu/gulab_jamun/2.avif'
    menu3.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu3.price = '265'

    menu4 = menuitem()
    menu4.name = 'Bread Gulab Jamun'
    menu4.img = 'menu/gulab_jamun/3.avif'
    menu4.det = 'LIFE IS SWEETER WITH A SPRINKLE OF INDULGENCE.'
    menu4.price = '370'

    menu5 = menuitem()
    menu5.name = 'Milk Gulab Jamun'
    menu5.img = 'menu/gulab_jamun/4.avif'
    menu5.det = 'LIFE IS SWEETER WITH A SPRINKLE OF INDULGENCE.'
    menu5.price = '450'

    menu6 = menuitem()
    menu6.name = 'Chocolate Gulab Jamun'
    menu6.img = 'menu/gulab_jamun/5.avif'
    menu6.det = 'LIFE IS SWEETER WITH A SPRINKLE OF INDULGENCE.'
    menu6.price = '200'

    menu7 = menuitem()
    menu7.name = 'Mango Gulab Jamun'
    menu7.img = 'menu/gulab_jamun/6.avif'
    menu7.det = 'LIFE IS SWEETER WITH A SPRINKLE OF INDULGENCE.'
    menu7.price = '200'

    menu8 = menuitem()
    menu8.name = 'Stuffed Gulab Jamun'
    menu8.img = 'menu/gulab_jamun/7.avif'
    menu8.det = 'LIFE IS SWEETER WITH A SPRINKLE OF INDULGENCE.'
    menu8.price = '200'


    menus=[menu1,menu2,menu3,menu4,menu5,menu6,menu7,menu8]
    webd = [awebd]
    webds = [webd1, webd2]
    if usercheck == True:
        print("if")
        print(otherpage)
        return render(request,'menu.html',{'menus':menus,'offer':offer,'webd':webd,'webds':webds,'otherpage':otherpage,'listname':listname,'logor':logor,'menuslider':menuslider})
    else:
        return render(request, 'menu.html', {'menus': menus, 'offer': offer, 'webd': webd, 'webds': webds,'listname':listname,'logor':logor,'menuslider':menuslider})

def Pastry(request):

    global otherpage,listname
    check(request)
    listname="Pastry"

    offer= offers()
    offer.name='Get 50% off on Your First Order'

    menu1=menuitem()
    menu1.name='Strawberry Pastry'
    menu1.img='menu/pastry/1.jpg'
    menu1.det='FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu1.price='200'

    menu2 = menuitem()
    menu2.name = 'Butterscotch Pastry'
    menu2.img = 'menu/pastry/2.jpg'
    menu2.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu2.price = '470'

    menu3 = menuitem()
    menu3.name = 'Truffle Pastry'
    menu3.img = 'menu/pastry/8.jpg'
    menu3.det = 'FOOD TASTES BETTER WHEN YOU ARE IN GOOD LOCATION.'
    menu3.price = '265'

    menu4 = menuitem()
    menu4.name = 'Pista Pastry'
    menu4.img = 'menu/pastry/3.jpg'
    menu4.det = 'Life is batter with pastries.'
    menu4.price = '370'

    menu5 = menuitem()
    menu5.name = 'Blueberry Pastry'
    menu5.img = 'menu/pastry/4.jpg'
    menu5.det = 'Life is batter with pastries.'
    menu5.price = '450'

    menu6 = menuitem()
    menu6.name = 'Vanilla Velvet Pastry'
    menu6.img = 'menu/pastry/5.jpg'
    menu6.det = 'Life is batter with pastries.'
    menu6.price = '200'

    menu7 = menuitem()
    menu7.name = 'Raspberry Decadence Pastry'
    menu7.img = 'menu/pastry/6.jpg'
    menu7.det = 'Life is batter with pastries.'
    menu7.price = '200'

    menu8 = menuitem()
    menu8.name = 'Almond Elegance Pastry'
    menu8.img = 'menu/pastry/7.jpg'
    menu8.det = 'Life is batter with pastries.'
    menu8.price = '200'


    menus=[menu1,menu2,menu3,menu4,menu5,menu6,menu7,menu8]
    webd = [awebd]
    webds = [webd1, webd2]
    if usercheck == True:
        print("if")
        print(otherpage)
        return render(request,'menu.html',{'menus':menus,'offer':offer,'webd':webd,'webds':webds,'otherpage':otherpage,'listname':listname,'menuslider':menuslider})
    else:
        return render(request, 'menu.html', {'menus': menus, 'offer': offer, 'webd': webd, 'webds': webds,'listname':listname,'menuslider':menuslider})

def gallery(request):
    global otherpage
    check(request)



    webd = [awebd]
    webds = [webd1, webd2]
    if usercheck==True:
        print(otherpage)
        return render(request,'gallery.html',{'gallery':gallery,'webd':webd,'webds':webds,'otherpage':otherpage,'logor':logor})
    else:
        return render(request, 'gallery.html',
                      {'gallery': gallery, 'webd': webd, 'webds': webds,'logor':logor})

def page(request):
    global imglogin
    global aboutr
    webd = [awebd]
    webds = [webd1, webd2]
    return render(request,'login.html',{'webd':webd,'webds':webds,'imglogin':imglogin,'logor':logor})

def register(request):
    webd = [awebd]
    webds = [webd1, webd2]
    return render(request,'register.html',{'webd':webd,'webds':webds,'logor':logor})

def reservation(request):
    global otherpage,reservation
    check(request)
    webd = [awebd]
    webds = [webd1, webd2]
    reservation=reservation1()
    reservation.mname='Reservation'
    reservation.det='Ghaziabad:'
    reservation.desc='KIET Group of Institutions'
    reservation.addr='Delhi-NCR'
    reservation.pin='Pin: 201206'
    reservation.phone='+91-8840854918'
    reservation.email='rohiit.chaurasiya@gmail.com'
    if usercheck==True:
        print(otherpage)
        return render(request,'reservation.html',{'reservation':reservation,'webd':webd,'webds':webds,'otherpage':otherpage,'logor':logor})
    else:
        return render(request, 'reservation.html', {'reservation': reservation, 'webd': webd, 'webds': webds,'logor':logor})

def add(request):
    global imglogin
    webd = [awebd]
    webds = [webd1, webd2]
    if request.method=='POST':
        username = request.POST["username"]
        # name = request.POST["name"]
        email = request.POST["email"]
        # phone = request.POST["phone"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        # dob = request.POST["dob"]
        # address = request.POST["address"]
        # city = request.POST["city"]
        # pin = request.POST["pin"]
        if pass1==pass2:
            if new_user.objects.filter(username=username).exists():
                return render(request, 'register.html', {'namerror':"User Name Already Exist Please try another userName",'webd': webd, 'webds': webds,'logor':logor})
            elif new_user.objects.filter(email=email).exists():
                return render(request, 'register.html', {'mailerror':"Eamil has already registerd",'webd': webd, 'webds': webds,'logor':logor})
            # elif new_user.objects.filter(phone=phone).exists():
            #     return render(request, 'register.html', {'phoneerror':"Phone No has already registerd",'webd': webd, 'webds': webds,'logor':logor})
            else:
                newinfo = new_user(username=username, email=email, pass1=pass1, pass2=pass2,
                           )
                new_user.user = request.user
                newinfo.save()
                return render(request, "login.html",{'webd':webd,'webds':webds,'imglogin':imglogin,'logor':logor})
        else:
            return render(request, "register.html", {'perror':"Password does not match",'webd': webd, 'webds': webds,'logor':logor})
    else:
        return render(request, 'register.html',{'webd':webd,'webds':webds,'logor':logor})

def reserv(request):
    global usercheck,imglogin,reservation,otherpage
    webd = [awebd]
    webds = [webd1, webd2]
    if usercheck==True:
        if request.method == 'POST':
            cname = request.POST["cname"]
            cemail = request.POST["cemail"]
            date = request.POST["date"]
            cphone = request.POST["cphone"]
            ctime = request.POST["ctime"]
            cperson = request.POST["cperson"]
            aphone = request.POST["aphone"]
            room = request.POST["room"]
            reservc = reservationb(cname=cname, cemail=cemail, date=date, cphone=cphone, ctime=ctime, cperson=cperson ,aphone=aphone,room=room,username=otherpage)
            reservationb.user = request.user
            reservc.save()
            return render(request, "reservation.html", {'webd': webd, 'webds': webds,'otherpage':otherpage,'reservation':reservation,'logor':logor})
        else:
            return render(request, 'reservation.html', {'webd': webd, 'webds': webds,'reservation':reservation,'logor':logor})
    else:
        return render(request, 'login.html', {'webd': webd, 'webds': webds,'imglogin':imglogin,'logor':logor})

def myreserv(request):
    global usercheck, imglogin, reservation, otherpage
    webd = [awebd]
    webds = [webd1, webd2]
    roomuser=[]
    for p in reservationb.objects.raw('SELECT * FROM homedelivery_reservationb where username=%s', [otherpage]):
        x = p
        roomuser.append(x)
    if roomuser==[]:
        print("Blank ")
        return render(request, 'room.html',{'webd': webd, 'webds': webds, 'otherpage': otherpage,'logor':logor,'ucart':ucart,})
    else:
        global room
        room = "cart"
        print(room)
        return render(request, 'room.html',
                      {'webd': webd, 'webds': webds, 'otherpage': otherpage, 'roomuser': roomuser, 'room': room,'logor':logor})


def userlogout(request):
    global usercheck , imglogin
    webd = [awebd]
    webds = [webd1, webd2]
    usercheck=False
    return render(request, 'login.html', {'webd': webd, 'webds': webds,'imglogin':imglogin,'logor':logor})

def additem(request):
    global usercheck , otherpage,nameul,priceul,qtyul,totalprice,amount
    nameul = request.POST.get("item_id")
    priceul = request.POST.get("price_id")
    qtyul = request.POST.get("qty")
    webd = [awebd]
    webds = [webd1, webd2]
    print("start user")
    if request.method=='POST':
        print(nameul)
        print(priceul)
        print(qtyul)
    if usercheck==True:
        y = int(qtyul or 0)
        z = int(priceul or 0)
        a = int(y * z)
        neworder=user_cart(item_name=nameul,price=a,qty=qtyul,username=otherpage)
        user_cart.user=request.user
        neworder.save()
        print("user order save")
        global orders
        userorderlist(request)
        cart1="cart"
        totalprice=0
        for p in user_cart.objects.raw('SELECT * FROM restaurants.homedelivery_user_cart where username=%s',[otherpage]):
            x = p
            totalprice = totalprice + int(p.price)

        amount=totalprice*100
        return render(request, 'order.html', {'webd': webd, 'webds': webds, 'otherpage': otherpage, 'orders': orders,'cart1':cart1,'logor':logor,'totalprice':totalprice,'amount':amount})
    else:
        return render(request, 'login.html', {'webd': webd, 'webds': webds,'imglogin':imglogin,'logor':logor})

def userorderlist(request):
    webd = [awebd]
    webds = [webd1, webd2]
    global otherpage, nameul, priceul, qtyul,totalprice,amount
    global orders ,price
    orders = []
    totalprice = 1
    for p in user_cart.objects.raw('SELECT * FROM restaurants.homedelivery_user_cart where username=%s', [otherpage]):
        x = p
        totalprice = totalprice + int(p.price)
        orders.append(x)


    if orders==[]:
        print("Blank ")
        return render(request, 'order.html',{'webd': webd, 'webds': webds, 'otherpage': otherpage,'orders': orders,'ucart':ucart,'logor':logor})
    else:
        name = request.POST.get('name')
        amount = 1000
        totalprice = totalprice - 1
        amount = (totalprice) * 100
        client = razorpay.Client(
            auth=("rzp_test_fK6V4JrgIbcHdj", "JZdV8Tv1crpbhnZCTRRMKCj1"))
        callback_url = 'http://' + str(get_current_site(request)) + "/payment/"
        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
        order_id = payment['id']
        print(callback_url)
        global cart1
        cart1 = "cart"
        print(cart1)
        return render(request, 'order.html',
                      {'webd': webd, 'webds': webds, 'otherpage': otherpage, 'orders': orders, 'cart1': cart1,'logor':logor,'totalprice':totalprice,
                       'callback_url':callback_url,'payment':payment,'order_id':order_id})


def finalitems(request): #your orders Button function
     global cart1 ,ucart
     global order,finalorder
     finalorder="My Orders"
     webd = [awebd]
     webds = [webd1, webd2]
     orders = []
     for p in user_orders.objects.raw('SELECT * FROM restaurants.homedelivery_user_orders where username=%s', [otherpage]):
         x = p
         orders.append(x)
     if orders == []:
         print("Blank ")
         return render(request, 'order.html',
                       {'webd': webd, 'webds': webds, 'otherpage': otherpage, 'orders': orders, 'ucart': ucart,'finalorder':finalorder,'logor':logor})
     else:
         global cart1
         cart1 = "cart"
         print(cart1)
         return render(request, 'order.html',
                       {'webd': webd, 'webds': webds, 'otherpage': otherpage, 'orders': orders, 'cart1': cart1,'finalorder':finalorder,'logor':logor})

def itemremove(request):
    global cart1 ,otherpage,amount
    nameul = request.POST.get("item_id")
    webd = [awebd]
    webds = [webd1, webd2]
    print("start user")
    if request.method == 'POST':
        usercart=user_cart.objects.filter(id=nameul).delete()
        user_cart.user=request.user
        print(nameul)
        orders = []
        totalprice=0
        for p in user_cart.objects.raw('SELECT * FROM restaurants.homedelivery_user_cart where username=%s', [otherpage]):
            x = p
            totalprice = totalprice + int(p.price)
            orders.append(x)
        if orders == []:
            print("Blank ")
            return render(request, 'order.html',
                          {'webd': webd, 'webds': webds, 'otherpage': otherpage, 'ucart': ucart, 'orders': orders,'logor':logor})
        else:
            global cart1
            cart1 = "cart"
            amount=totalprice*100
            return render(request, 'order.html',
                          {'webd': webd, 'webds': webds, 'otherpage': otherpage, 'orders': orders, 'cart1': cart1,'logor':logor,'totalprice':totalprice,'amount':amount})
    else:
        return render(request, 'order.html',{'webd': webd, 'webds': webds, 'otherpage': otherpage,'logor':logor})

def orderconfirm(request):
    global orders
    webd = [awebd]
    webds = [webd1, webd2]
    global orders,totalprice
    orders = []
    totalprice=0
    for p in user_cart.objects.raw('SELECT * FROM restaurants.homedelivery_user_cart where username=%s', [otherpage]):
        x = p
        totalprice=totalprice+int(p.price)
        orders.append(x)
    print(totalprice)
    return render(request, 'payment.html',{'webd': webd, 'webds': webds, 'otherpage': otherpage, 'ucart': ucart, 'cart1': cart1,'orders': orders,'totalprice':totalprice
                                           ,'userpayment':userpayment,'logor':logor})

@csrf_exempt
def payment(request):
    if request.method == 'POST':
        webd = [awebd]
        webds = [webd1, webd2]
        global userpayment
        userpayment='Paid'
        print(userpayment)
        fitems = []
        fprice = []
        fqty = []
        for p in user_cart.objects.raw('SELECT * FROM restaurants.homedelivery_user_cart where username=%s',[otherpage]):
            x = p.item_name
            y = p.price
            z = p.qty
            fitems.append(x)
            fprice.append(y)
            fqty.append(z)
            finalorder = user_orders(item_name=p.item_name, price=p.price, qty=p.qty, username=otherpage,
                                     payment=userpayment)
            user_cart.user = request.user
            finalorder.save()
            print("user order save")
        usercartdelete = user_cart.objects.filter(username=otherpage).delete()
        user_cart.user = request.user
        userpayment = 'False'
        return render(request, 'payment.html',{'webd': webd, 'webds': webds,'userpayment':userpayment,'logor':logor,'otherpage': otherpage, 'ucart': ucart,})
    else:
        return HttpResponse('Payment Error')


def render_to_response(param, csrfContext):
    pass


def orderplace(request):
    global cart1,userpayment
    global order, finalorder
    finalorder = "My Order"
    porder = orderplaceimg()
    porder.img = 'place.png'
    webd = [awebd]
    webds = [webd1, webd2]
    fitems = []
    fprice=[]
    fqty=[]
    for p in user_cart.objects.raw('SELECT * FROM restaurants.homedelivery_user_cart where username=%s', [otherpage]):
        x = p.item_name
        y=p.price
        z=p.qty
        fitems.append(x)
        fprice.append(y)
        fqty.append(z)
        finalorder= user_orders(item_name=p.item_name, price=p.price, qty=p.qty, username=otherpage,payment=userpayment)
        user_cart.user = request.user
        finalorder.save()
        print("user order save")
    usercartdelete = user_cart.objects.filter(username=otherpage).delete()
    user_cart.user = request.user
    userpayment='False'
    return render(request, 'orderplace.html', {'webd': webd, 'webds': webds,'otherpage':otherpage,'porder':porder,'logor':logor})


def finalorderplace(request):
    global porder
    porder = orderplaceimg()
    porder.img = 'place.png'
    webd = [awebd]
    webds = [webd1, webd2]
    return render(request, 'orderplace.html',{'webd': webd, 'webds': webds,'porder':porder,'ucart':ucart,'logor':logor})

def admin(request):
    global adminimg

    admin="Administrative"
    adminimg = adminloginpage()
    adminimg.img = 'admin.png'
    return render(request, 'adminpage.html',{'adminimg':adminimg,'admin':admin,'logor':logor})

def administrative(request):
    webd = [awebd]
    webds = [webd1, webd2]
    return render(request, 'admin.html', {'webd': webd, 'webds': webds,'logor':logor})

admincheck=False
def checkadmin(request):
    global adminempty
    adminempty = cart()
    adminempty.img = 'cart.png'
    webd = [awebd]
    webds = [webd1, webd2]
    print("admiin page")
    if request.method == 'POST':
        fpassword1 = request.POST['pass1']
        fadminname = request.POST['username']
        if adminlogin.objects.filter(username=fadminname).exists() and new_user.objects.filter(pass1=fpassword1).exists():
            global otherpage
            otherpage=fadminname
            admincheck = True
            print(fadminname)
            print("success1")
            userorders = []
            for p in user_orders.objects.raw('SELECT * FROM restaurants.homedelivery_user_orders where status="Processing..." '):
                x = p
                userorders.append(x)
            if userorders == []:
                print("Blank ")
                return render(request, 'adminorder.html',{'webd': webd, 'webds': webds, 'otherpage': otherpage, 'userorders': userorders,'adminempty':adminempty,'logor':logor})
            else:
                global adminorders
                adminorders = "cart"
                print(adminorders)
                return render(request, 'adminorder.html',{'webd': webd, 'webds': webds, 'otherpage': otherpage, 'userorders': userorders,'adminorders':adminorders,'adminempty':adminempty,'logor':logor})
        else:
            print("worng password or username")
            return render(request, 'admin.html', {'webd': webd, 'webds': webds,'logor':logor})
    else:
        return render(request, 'adminpage.html', {'webd': webd, 'webds': webds,'adminimg':adminimg,'logor':logor})


def cancel(request):
    global otherpage,adminorders
    print("cancel Page")
    nameul = request.POST.get("item_id")

    webd = [awebd]
    webds = [webd1, webd2]

    print(nameul)
    if request.method == 'POST':
        usercart = user_orders.objects.filter(id=nameul).delete()
        user_orders.user = request.user
        print(nameul)
        userorders = []
        for p in user_orders.objects.raw('SELECT * FROM restaurants.homedelivery_user_orders where status="Processing..."'):
            x = p
            userorders.append(x)
        print(userorders)
        if userorders == []:
            print("Blank")
            return render(request, 'adminorder.html',
                          {'webd': webd, 'webds': webds, 'otherpage': otherpage, 'adminempty': adminempty,'logor':logor})
        else:
            global adminorders
            adminorders = "cart"
            print(adminorders)
            return render(request, 'adminorder.html',
                          {'webd': webd, 'webds': webds, 'otherpage': otherpage, 'userorders': userorders,'adminorders': adminorders,'logor':logor})
    else:
        print("post error")
        return render(request, 'adminorder.html', {'webd': webd, 'webds': webds, 'otherpage': otherpage,'logor':logor})


def admindelivered(request):
    nameul = request.POST.get("item_id")
    itemul = request.POST.get("itemname")
    priceul = request.POST.get("price")
    qtyul = request.POST.get("qty")
    userul = request.POST.get("username")
    paymentul = request.POST.get("payment")
    webd = [awebd]
    webds = [webd1, webd2]
    status='Delivered'
    if request.method == 'POST':
        adminconfirm = user_orders(id=nameul,username=userul,price=priceul,qty=qtyul,item_name=itemul,payment=paymentul)
        adminconfirm.status='Delivered'
        user_orders.user = request.user
        adminconfirm.save()
        print(nameul)
        userorders = []


        for p in user_orders.objects.raw('SELECT * FROM restaurants.homedelivery_user_orders where status="Processing..."'):
            x = p
            userorders.append(x)
        if userorders == []:
            print("Blank")
            return render(request, 'adminorder.html',
                          {'webd': webd, 'webds': webds, 'otherpage': otherpage, 'adminempty': adminempty,'logor':logor})
        else:
            global adminorders
            adminorders = "cart"
            print(adminorders)
            return render(request, 'adminorder.html',
                          {'webd': webd, 'webds': webds, 'otherpage': otherpage, 'userorders': userorders,'adminorders': adminorders,'logor':logor})
    else:
        print("post error")
        return render(request, 'adminorder.html', {'webd': webd, 'webds': webds, 'otherpage': otherpage,'adminempty': adminempty,'logor':logor})

