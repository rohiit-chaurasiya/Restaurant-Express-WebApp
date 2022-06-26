from django.db import models

# Create your models here.
class new_info(models.Model):
    username= models.CharField(max_length=30)
    name=models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    pass1=models.CharField(max_length=30)
    pass2= models.CharField(max_length=30)
    dob = models.CharField(max_length=15)
    address= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    pin = models.CharField(max_length=12)

class adminlogin(models.Model):
    username= models.CharField(max_length=30)
    email= models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    pass1=models.CharField(max_length=30)
    pass2 = models.CharField(max_length=30)

class rlogo:
    id:int
    img:str

class item:
    id : int
    name : str
    img : str
    det : str
    price : str
    skill1 : str
    skill2: str
    skill3: str
    skill4: str
    skill5: str

class aboutd:
    id:int
    name:str
    img:str
    det:str
    desc:str

class bottom:
    id : int
    name : str
    det : str
    img1 : str
    img2 : str
    op1 : str
    op2: str
    op3: str
    op4: str
    op5: str

class offers:
    id: int
    name: str
    det: str

class menuitem:
    id: int
    name: str
    det: str
    img: str
    price:int

class gallery1:
    id: int
    name: str
    det: str
    img: str

class reservation1:
    id:int
    mname:str
    det: str
    desc:str
    phone:str
    emanil:str
    addr:str
    pin:str

class reservationb(models.Model):
    username = models.CharField(max_length=50,default='')
    cname = models.CharField(max_length=50)
    date = models.CharField(max_length=15)
    cemail = models.CharField(max_length=50)
    cphone = models.CharField(max_length=10)
    ctime = models.CharField(max_length=10)
    cperson = models.CharField(max_length=3)
    aphone = models.CharField(max_length=12,default='')
    room = models.CharField(max_length=2,default='1')

class user_cart(models.Model):
    username= models.CharField(max_length=50)
    item_name= models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    qty=models.CharField(max_length=10)


class user_orders(models.Model):
    username= models.CharField(max_length=50)
    item_name= models.CharField(max_length=50)
    price = models.CharField(max_length=12)
    qty=models.CharField(max_length=30)
    payment=models.CharField(max_length=20,default='')
    status = models.CharField(max_length=20, default='Processing...')



class cart:
    img : str

class orderplaceimg:
    img:str

class adminloginpage:
    img:str

class loginimg:
    img:str
