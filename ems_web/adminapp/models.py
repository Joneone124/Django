from django.db import models

# Create your models here.

class Admin(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    sex = models.BooleanField(default=True)

class aaa(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

class Emp(models.Model):
    name = models.CharField(max_length=20)
    salary = models.SmallIntegerField()
    age = models.SmallIntegerField()
    head = models.FileField(upload_to='imgs')