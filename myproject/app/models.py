from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import pandas as pd




# Create your models here.
class Trans(models.Model):
    id          =   models.AutoField(primary_key=True)
    name        =   models.CharField(max_length=255)
    password    =   models.CharField(max_length=256)
    cname       =   models.CharField(max_length=255)
    address     =   models.CharField(max_length=128)
    gst         =   models.DecimalField("GST", max_digits=10, decimal_places=2, default='0.00', blank=True, null=False)
    contactno   =   models.CharField(max_length=225)
    contactperson   =   models.CharField(max_length=255)

    image = models.FileField(upload_to='upload', null=True)
          
    created_date = models.DateField(auto_now_add=True)  # Changed auto_now_added to auto_now_add
    is_active = models.BooleanField(default=True)  # Changed to BooleanField for boolean values


class Register(models.Model):
    id           =  models.AutoField(primary_key=True)
    
    cname        =  models.CharField(max_length=255)
    address      =  models.CharField(max_length=255)
    gst          =   models.DecimalField("GST", max_digits=10, decimal_places=2, default='0.00', blank=True, null=False)
    contactno    =   models.CharField(max_length=12)
    contactperson   =   models.CharField(max_length=12)
    transId         = models.ForeignKey(Trans, on_delete=models.CASCADE, blank=True, null=True)

    
    created_date = models.DateField(auto_now_add=True)  # Changed auto_now_added to auto_now_add
    is_active = models.BooleanField(default=True)  # Changed to BooleanField for boolean values
    
    
class Employee(models.Model):
        id          =   models.AutoField(primary_key=True)
        name        =   models.CharField(max_length=255)
        password    =   models.CharField(max_length=255)
        email       =   models.EmailField(max_length=255)
        phone       =   models.CharField(max_length=255)
        registerId = models.ForeignKey(Register, on_delete=models.CASCADE, blank=True)
        

        
        created_date = models.DateField(auto_now_add=True)  # Changed auto_now_added to auto_now_add
        is_active = models.BooleanField(default=True)  # Changed to BooleanField for boolean values
    
class authtoken_token(models.Model):
        id          =   models.AutoField(primary_key=True)
        

        
        
class login(models.Model):
    id          =   models.AutoField(primary_key=True)
    name        =   models.CharField(max_length=255)
    password    =   models.CharField(max_length=256)
    


class Truck(models.Model):
    id          =   models.AutoField(primary_key=True)
    dname       =   models.CharField(max_length=255)
    dcontact    =   models.CharField(max_length=255)
    truckno     =   models.CharField(max_length=10)
    oname       =   models.CharField(max_length=255)
    ocontact    =   models.CharField(max_length=12,blank=True)
    Ttype       =   models.CharField(max_length=255) 
    transId = models.ForeignKey(Trans, on_delete=models.CASCADE, blank=True)
    
    created_date = models.DateField(default=datetime.now)  # Changed auto_now_added to auto_now_add
    is_active = models.BooleanField(default=True)  # Changed to BooleanField for boolean values

class Worker(models.Model):
    id          =   models.AutoField(primary_key=True)
    lname       =   models.CharField(max_length=255)
    address     =   models.CharField(max_length=128)
    contactno    =   models.CharField(max_length=255)
    transId = models.ForeignKey(Trans, on_delete=models.CASCADE, blank=True)

    created_date = models.DateField(auto_now_add=True)  # Changed auto_now_added to auto_now_add
    is_active = models.BooleanField(default=True)  # Changed to BooleanField for boolean values
    


    
class Billing(models.Model):   
    id          =   models.AutoField(primary_key=True)
    name        =   models.CharField(max_length=255, null=True)
    address     =   models.CharField(max_length=128, null=True)
    gst         = models.CharField(max_length=20,null=True)  # Corrected gst field
    c_inv_no = models.CharField(max_length=20, null=True)
    fy             = models.CharField(max_length=20, null=True)
    inv_no         = models.CharField(max_length=20,null=True)
    inv_date       = models.DateField(null=True)
    c_date      = models.CharField(max_length=255,null=True)
    From        =   models.CharField(max_length=255,null=True)
    To          =   models.CharField(max_length=255, null=True)
    truck = models.CharField(max_length=20, blank=True)
    Lr_no       =   models.CharField(max_length=255,null=True)
    Dsicriptions=   models.CharField(max_length=255,null=True)
    Qty_weight  =   models.CharField(max_length=255,null=True)
    Rate        =   models.CharField(max_length=255, null=True)
    Amount      =   models.CharField(max_length=255,null=True)
    created_date = models.DateField(auto_now_add=True)  # Changed auto_now_added to auto_now_add
    is_active = models.BooleanField(default=True)  # Changed to BooleanField for boolean values

def __str__(self):
    return self.name


# class Billing(models.Model):   
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=128)
#     gst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=False)  # Corrected gst field
#     source = models.CharField(max_length=255)  # Renamed 'From' to 'source'
#     destination = models.CharField(max_length=255)  # Renamed 'To' to 'destination'
#     lr_no = models.CharField(max_length=255)
#     truck = models.ForeignKey(Truck, on_delete=models.CASCADE, blank=True)
#     descriptions = models.CharField(max_length=255)  # Corrected typo
#     qty_weight = models.IntegerField(null=True)
#     rate = models.CharField(max_length=255)
#     amount = models.IntegerField(null=True)
    
#     created_date = models.DateField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100)

