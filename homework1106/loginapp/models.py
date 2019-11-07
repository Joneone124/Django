from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Employee(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Department(models.Model):
    name = models.CharField(max_length=20)