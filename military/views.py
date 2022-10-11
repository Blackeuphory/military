from django.shortcuts import render
from military.models import UnitType,Crew,Weapon,Vehicle,Unit
from django.views import View
# Create your views here.

class AddUnitTypeView(View):
    def get(self,request):
        unit_type=UnitType.objects.all().order_by('name')
        return render(request,'unit_type.html',{'unit_type':unit_type})
    def post(self,request):
        name=request.POST['type']
        x=UnitType(name=name)
        return render(request,'unit_type.html',{'message':'rodzaj dodany'})


class AddWeaponView(View):
    def get(self,request):
        weapon=Weapon.objects.all().order_by('name')
        return render(request,'weapon.html', {'weapon':weapon})