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
    assert 'Wojsko' in str(response.content)

@pytest.mark.django_db
def test_add_unit_type_post():
    client=Client()
    url= reverse('unit_type')
    data = {
        'name': 'Jednostka Specjalna',
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(url)
    assert UnitType.objects.get(name='slawek')