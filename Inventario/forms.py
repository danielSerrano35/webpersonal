from django import forms
from .models import Venta
 
class vender_auto(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
class form_venta(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update({'autocomplete': 'off'})
    class Meta:
        model = Venta