from django.contrib import admin
from military.models import UnitType,Crew,Weapon,Vehicle,Unit
# Register your models here.
admin.site.register(UnitType),
admin.site.register(Crew),
admin.site.register(Weapon),
admin.site.register(Vehicle)