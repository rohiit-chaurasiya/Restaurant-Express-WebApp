from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)



class new_user(models.Model):
    username= models.CharField(max_length=30)
    name=models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    pass1=models.CharField(max_length=30)
    pass2= models.CharField(max_length=30)
    dob = models.CharField(max_length=15)


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
