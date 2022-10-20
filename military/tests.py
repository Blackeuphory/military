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
    # assert 'military' in str(response.content)

@pytest.mark.django_db
def test_add_unit_type_post():
    client=Client()
    url= reverse('unit_type')
    data = {
        'type': 'pancerna',
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert UnitType.objects.get(name='pancerna')


@pytest.mark.django_db
def test_add_weapon_post():
    client = Client()
    url = reverse('weapon')
    data = {
        'weapon': 'AK 12',


    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert Weapon.objects.get(name='AK 12')


@pytest.mark.django_db
def test_add_vehicle_post():
    client = Client()
    url = reverse('vehicle')
    data = {
        'vehicle': 'K2 Black Panther',

    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert Vehicle.objects.get(name='K2 Black Panther')


@pytest.mark.django_db
def test_add_crew_post():
    client = Client()
    url = reverse('add_crew')
    data = {
        'crew': 'Księgowa',

    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert Crew.objects.get(name='Księgowa')
@pytest.mark.django_db
def test_add_unit_get():
    client = Client()
    url = reverse('add_unit')
    response = client.get(url)
    form_in_view = response.context['form']
    assert response.status_code == 200
    assert isinstance(form_in_view, UnitCreateForm)
def test_add_unit_post():# nie działa
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
    response = client.post(url,data)
    assert response.status_code == 200
    assert Unit.objects.post(name='1 Brygada', weapon='HK416',
                            vehicle='Leopard 2PL', parent='1 Dywizja',crew='Ksiegowa',type='Kawaleria Powietrzna')

@pytest.mark.django_db
def test_all_unit_get():
        client = Client()
        url = reverse('show_unit')
        response = client.get(url)

        unit_form_view = response.context['units']
        assert response.status_code == 200


@pytest.mark.django_db
def test_all_weapon_get():
        client = Client()
        url = reverse('show_weapon')
        response = client.get(url)

        weapon_form_view = response.context['weapons']
        assert response.status_code == 200


@pytest.mark.django_db
def test_all_vehicle_get():
        client = Client()
        url = reverse('show_vehicle')
        response = client.get(url)

        vehicle_form_view = response.context['vehicles']
        assert response.status_code == 200

@pytest.mark.django_db
def test_all_type_get():
        client = Client()
        url = reverse('show_type')
        response = client.get(url)

        type_form_view = response.context['types']
        assert response.status_code == 200
