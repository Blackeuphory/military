from django.db import models


# Create your models here.

class UnitType(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

class Crew(models.Model):
    name = models.CharField(max_length=125)
    def __str__(self):
        return self.name

class Weapon(models.Model):
    name=models.CharField(max_length=125)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name=models.CharField(max_length=125)
    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=125)
    type = models.ForeignKey(UnitType,on_delete=models.CASCADE)
    parent = models.ForeignKey('Unit', null=True,on_delete=models.CASCADE,blank=True)
    crew = models.ManyToManyField(Crew)
    weapon=models.ManyToManyField(Weapon)
    vehicle=models.ManyToManyField(Vehicle)

    def __str__(self):
        return self.name