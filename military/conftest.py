import pytest
from military.models import UnitType
@pytest.fixture
def unit_type():
    return UnitType.objects.create(name='Kawaleria Powietrzna')
