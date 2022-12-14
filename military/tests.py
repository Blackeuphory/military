import pytest
from django.test import Client
from django.urls import reverse
from military.forms import UnitCreateForm
from military.models import UnitType,Crew,Weapon,Vehicle,Unit

@pytest.mark.django_db
def test_index_get():
    client = Client()
    url = ''
    response = client.get(url)
    assert response.status_code == 200
    # assert 'military' in str(response.content)

@pytest.mark.django_db
def test_index_post():
    client = Client()
    url = ''
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_unit_type_get():
    client = Client()
    url = reverse('unit_type')
    response = client.get(url)
    assert response.status_code == 200



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
def test_add_weapon_get():
    client = Client()
    url = reverse('weapon')
    response = client.get(url)
    assert response.status_code == 200

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
def test_add_vehicle_get():
    client = Client()
    url = reverse('vehicle')
    response = client.get(url)
    assert response.status_code == 200


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
def test_add_crew_get():
    client = Client()
    url = reverse('add_crew')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_crew_post():
    client = Client()
    url = reverse('add_crew')
    data = {
        'crew': 'Ksi??gowa',

    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert Crew.objects.get(name='Ksi??gowa')
@pytest.mark.django_db
def test_add_unit_get():
    client = Client()
    url = reverse('add_unit')
    response = client.get(url)
    form_in_view = response.context['form']
    assert response.status_code == 200
    assert isinstance(form_in_view, UnitCreateForm)
@pytest.mark.django_db
def test_add_unit_post(unit_type):
    client = Client()
    url = reverse('add_unit')
    data ={
        'name': '1 Brygada',
        'type': unit_type.id
    }
    response = client.post(url,data)
    assert response.status_code == 200
    form=response.context['form']
    print(form.errors)
    assert Unit.objects.get(name='1 Brygada')

@pytest.mark.django_db
def test_all_unit_get():
        client = Client()
        url = reverse('show_unit')
        response = client.get(url)

        unit_form_view = response.context['units']
        assert response.status_code == 200
@pytest.mark.django_db
def test_all_unit_post():
    client = Client()
    url = reverse('show_unit')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_all_weapon_get():
        client = Client()
        url = reverse('show_weapon')
        response = client.get(url)

        weapon_form_view = response.context['weapons']
        assert response.status_code == 200
@pytest.mark.django_db
def test_all_weapon_post():
    client = Client()
    url = reverse('show_weapon')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_all_vehicle_get():
        client = Client()
        url = reverse('show_vehicle')
        response = client.get(url)

        vehicle_form_view = response.context['vehicles']
        assert response.status_code == 200

@pytest.mark.django_db
def test_all_vehicle_post():
    client = Client()
    url = reverse('show_vehicle')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_all_type_get():
        client = Client()
        url = reverse('show_type')
        response = client.get(url)

        type_form_view = response.context['types']
        assert response.status_code == 200

@pytest.mark.django_db
def test_all_type_post():
    client = Client()
    url = reverse('show_type')
    response = client.get(url)
    assert response.status_code == 200
