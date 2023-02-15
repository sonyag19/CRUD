from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=100)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=30)


class Register(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    uname=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length=20)

class ItemModel(models.Model):
    iname=models.CharField(max_length=20)
    des=models.CharField(max_length=50)
    price = models.IntegerField()
    image=models.FileField(upload_to="crud_app/static")
