from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Brands(models.Model):
    name = models.TextField(max_length=50)
    Description1 = models.TextField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    logo = models.FileField(upload_to='media/brands',null=True,blank=True)
    img1 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img2 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img3 = models.FileField(upload_to='media/brands',null=True,blank=True)
    engine = models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    power =  models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    torque =  models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    mileage =  models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    weight =  models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    aboutcar = models.TextField(max_length=1000,null=True,blank=True)
    img4 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img5 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img6 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img7 = models.FileField(upload_to='media/brands',null=True,blank=True)
   


    def __str__(self):
        return self.name

class Bikes(models.Model):
    name = models.TextField(max_length=50)
    Description1 = models.TextField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    logo = models.FileField(upload_to='media/brands',null=True,blank=True)
    img1 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img2 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img3 = models.FileField(upload_to='media/brands',null=True,blank=True)
    engine = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    power =  models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    torque =  models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    mileage =  models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    weight =  models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    aboutcar = models.TextField(max_length=1000,null=True,blank=True)
    img4 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img5 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img6 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img7 = models.FileField(upload_to='media/brands',null=True,blank=True)
  
    def __str__(self):
        return self.name

class cars(models.Model):
    name = models.TextField(max_length=50)
    Description1 = models.TextField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    logo = models.FileField(upload_to='media/brands',null=True,blank=True)
    img1 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img2 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img3 = models.FileField(upload_to='media/brands',null=True,blank=True)
    engine = models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    power =  models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    torque =  models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    mileage =  models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    weight =  models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    aboutcar = models.TextField(max_length=1000,null=True,blank=True)
    img4 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img5 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img6 = models.FileField(upload_to='media/brands',null=True,blank=True)
    img7 = models.FileField(upload_to='media/brands',null=True,blank=True)
   

    def __str__(self):
        return self.name

class UserProfile(models.Model):

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=40)
    mobile = models.CharField(max_length=15)  
    address = models.TextField(max_length=1000)
    termcond = models.BooleanField()

    def __str__(self):
        return self.name

class deal(models.Model):
    pin = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)  

    def __str__(self):
        return self.name
