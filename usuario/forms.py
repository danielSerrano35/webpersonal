from django import forms
from django.contrib.auth.forms import AuthenticationForm
from usuario.models import Usuario

class FormularioLogin(AuthenticationForm): 
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormularioUser(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña...',
            'id': 'password1',
            'required': 'required',
            'autocomplete':'off',
        }
    ))
    password2 = forms.CharField(label = 'Contraseña de Confirmación', widget = forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña...',
            'id': 'password2',
            'required': 'required',
        }
    ))
    
    class Meta:
        model = Usuario
        fields = ('email', 'username', 'nombres', 'apellidos')
        widgets = {
            'email': forms.EmailInput( 
                attrs = { 
                    'class': 'form-control', 
                    'placeholder': 'Correo Electrónico', 
                }
            ), 
            'nombres': forms.TextInput( 
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                }
            ), 
            'apellidos': forms.TextInput(
                attrs = { 
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'username': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de usuario',
                }
            )
        }
    def contrasenia2(self):
        print(self.cleaned_data)
        password1 =self.cleaned_data.get('password1')
        password2 =self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2
    def save(self, commint =True):
        user = super().save(commit=False)
        user.set_password(self.changed_data['password1'])
        if commint:
            user.save()
        return user