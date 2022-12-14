"""projekt_koncowy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from military import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('unit_type/', views.AddUnitTypeView.as_view(),name='unit_type'),
    path('add_weapon/', views.AddWeaponView.as_view(), name='weapon'),
    path('add_crew/', views.AddCrewView.as_view(), name='add_crew'),
    path('add_vehicle/', views.AddVehicleView.as_view(), name='vehicle' ),
    path('add_unit/', views.AddUnitView.as_view(), name='add_unit'),
    path('', views.IndexView.as_view()),
    path('show_unit/', views.ShowUnitView.as_view(), name='show_unit'),
    path('show_weapon/', views.ShowWeaponView.as_view(), name='show_weapon'),
    path('show_vehicle/', views.ShowVehicleView.as_view(), name='show_vehicle'),
    path('show_type/', views.ShowTypeView.as_view(), name='show_type')
]
