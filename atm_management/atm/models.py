from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class account(models.Model):
    IFSC = models.CharField(max_length=250,)
    Ac_NO = models.IntegerField(primary_key=True,default=None)
    Ac_type = models.CharField(max_length=250)
    password = models.CharField(max_length=150)
    Balance = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True)

class Branch(models.Model):
    IFSC = models.CharField(max_length=250,primary_key=True)
    Branch_Name = models.TextField(max_length=250)

class Transaction(models.Model):
    Ac_NO = models.IntegerField(default=None)
    Date_and_time = models.DateTimeField(auto_now_add=True)
    Debit = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True)
    Credit = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    Balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
