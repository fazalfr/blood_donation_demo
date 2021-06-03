from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    age = models.IntegerField()
    number = models.IntegerField()


class Done(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    group = models.CharField(max_length=10)
    contact = models.IntegerField()
    district = models.CharField(max_length=30)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    photo = models.FileField()
