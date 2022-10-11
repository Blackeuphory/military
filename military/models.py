from django.db import models


# Create your models here.

class UnitType(models.Model):
    name = models.CharField(max_length=125)


class Crew(models.Model):
    name = models.CharField(max_length=125)


class Weapon(models.Model):
    name=models.CharField(max_length=125)

class Vehicle(models.Model):
    name=models.CharField(max_length=125)


class Unit(models.Model):
    name = models.CharField(max_length=125)
    type = models.ForeignKey(UnitType,on_delete=models.CASCADE)
    parent = models.ForeignKey('Unit', null=True,on_delete=models.CASCADE)
    crew = models.ManyToManyField(Crew)
    weapon=models.ManyToManyField(Weapon)
    vehicle=models.ManyToManyField(Vehicle)
