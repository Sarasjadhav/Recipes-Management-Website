from django.db import models


# Create your models here.

class Student(models.Model):
    # id=models.AutoField()   unique id by default set by django server
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    image=models.ImageField()
    file=models.FileField()
    
class Car(models.Model):
    car_name=models.CharField( max_length=100)
    car_speed=models.IntegerField()
    