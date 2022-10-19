import pytest
from django.test import Client
from django.urls import reverse
from military.forms import UnitCreateForm
from military.models import UnitType,Crew,Weapon,Vehicle,Unit

def test_index():
    client = Client()
    url = ''
    response = client.get(url)
    assert response.status_code == 200
    assert 'military' in str(response.content)

@pytest.mark.django_db
def test_add_unit_type_post():
    client=Client()
    url= reverse('unit_type/')
    data = {
        'name': 'Jednostka Specjalna',
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(url)
    assert UnitType.objects.get(name='pancerna')






@pytest.mark.django_db
def test_add_weapon_post():
    client = Client()
    url = reverse('add_weapon')
    data = {
        'name': 'AK 12',


    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Weapon.objects.get(name='AK 12')


@pytest.mark.django_db
def test_add_vehicle_post():
    client = Client()
    url = reverse('add_vehicle')
    data = {
        'name': 'K2 Black Panther',

    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Vehicle.objects.get(name='K2 Black Panther')


@pytest.mark.django_db
def test_add_crew_post():
    client = Client()
    url = reverse('add_crew')
    data = {
        'name': 'Księgowa',

    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Crew.objects.get(name='Księgowa')
@pytest.mark.django_db
def test_add_unit_get():
    client = Client()
    url = reverse('add_unit/')
    response = client.get(url)
    form_in_view = response.context['formularz']
    assert response.status_code == 302
    assert isinstance(form_in_view, UnitCreateForm)
def test_add_unit_post():
    client = Client()
    url = reverse('add_unit')
    data ={
        'name': '1 Brygada',
        'weapon': 'HK416',
        'vehicle': 'Leopard 2PL',
        'parent':'1 Dywizja',
        'crew': 'księgowa',
        'type': 'Kawaleria Powietrzna'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(url)
    assert Unit.objects.get(name='1 Brygada', weapon='HK416',
                            vehicle='Leopard 2PL', parent='1 Dywizja',crew='Ksiegowa',type='Kawaleria Powietrzna')

@pytest.mark.django_db
def test_all_unit_get(units):
        client = Client()
        url = reverse('show_unit/')
        response = client.get(url)

        unit_form_view = response.context['unit']
        assert response.status_code == 302
        assert unit_form_view.count() == len(units)

@pytest.mark.django_db
def test_all_weapon_get(weapon):
        client = Client()
        url = reverse('show_weapon/')
        response = client.get(url)

        weapon_form_view = response.context['weapon']
        assert response.status_code == 302
        assert weapon_form_view.count() == len(weapon)

@pytest.mark.django_db
def test_all_vehicle_get(vehicle):
        client = Client()
        url = reverse('show_vehicle/')
        response = client.get(url)

        vehicle_form_view = response.context['vehicle']
        assert response.status_code == 302
        assert vehicle_form_view.count() == len(vehicle)
@pytest.mark.django_db
def test_all_type_get(types):
        client = Client()
        url = reverse('show_type/')
        response = client.get(url)

        type_form_view = response.context['type']
        assert response.status_code == 302
        assert type_form_view.count() == len(types)