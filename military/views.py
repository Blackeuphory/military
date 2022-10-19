from django.shortcuts import render,redirect
from military.models import UnitType,Crew,Weapon,Vehicle,Unit
from django.views import View
from military.forms import UnitCreateForm
# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request, 'base.html')

class AddUnitTypeView(View):
    def get(self,request):
        unit_type=UnitType.objects.all().order_by('name')
        return render(request,'unit_type.html',{'unit_type':unit_type})
    def post(self,request):
        name=request.POST['type']
        ut=UnitType(name=name)
        ut.save()
        return render(request,'unit_type.html',{'message':'rodzaj dodany'})


class AddWeaponView(View):
    def get(self,request):
        weapon=Weapon.objects.all().order_by('name')
        return render(request,'weapon.html', {'weapon':weapon})

    def post(self,request):
        weapon=request.POST['weapon']
        w=Weapon(name=weapon)
        w.save()
        return render(request,'weapon.html', {'message':'uzbrojenie dodane'})

class AddCrewView(View):
    def get(self,request):
        crew=Crew.objects.all().order_by('name')
        return render(request,'crew.html', {'crew': crew})

    def post(self,request):
        crew=request.POST['crew']
        c=Crew(name=crew)
        c.save()
        return render(request,'crew.html', {'message':'załoga dodana'})

class AddVehicleView(View):
    def get(self,request):
        vehicle=Vehicle.objects.all().order_by('name')
        return render(request,'vehicle.html', {'vehicle': vehicle})

    def post(self,request):
        vehicle=request.POST['vehicle']
        v=Vehicle(name=vehicle)
        v.save()
        return render(request,'vehicle.html', {'message':'pojazd dodany'})

class AddUnitView(View):
    def get(self,request):
        form=UnitCreateForm()
        return render(request, 'unit.html', {'form':form})
    def post(self,request):
        form= UnitCreateForm(request.POST)

        if form.is_valid():
            form.save()

        return render(request, 'unit.html', {'form': form, 'message':'Jednostka dodana'})

class ShowUnitView(View):
    def get(self,request):
        units=Unit.objects.all()
        return render(request,'unit_list.html', {'units':units})

class ShowWeaponView(View):
    def get(self,request):
        weapons=Weapon.objects.all()
        return render(request, 'weapons_list.html', {'weapons':weapons})
class ShowVehicleView(View):
    def get(self,request):
        vehicles=Vehicle.objects.all()
        return render(request, 'vehicles_list.html', {'vehicles':vehicles})
class ShowTypeView(View):
    def get(self,request):
        types=UnitType.objects.all()
        return  render(request, 'type.html', {'types':types})
