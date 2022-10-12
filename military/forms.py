from django import forms
from  military.models import Unit

class UnitCreateForm(forms.ModelForm):
    class Meta:
        model=Unit
        fields='__all__'