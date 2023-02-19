from django import forms
from .models import Venta
 
class vender_auto(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'

class FormVenta(forms.ModelForm):

    class Meta:
        model = Venta
        fields = '__all__'
        """widgets = {
            'id_auto': forms.HiddenInput(
                attrs={
                    'required': False
                })
        }"""