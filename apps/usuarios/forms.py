from django import forms
from .models import Usuario
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["password", "username", "first_name", "last_name", "email", "is_active", "dni"]

class FormUser(UserCreationForm):
    # COmo customuzar los atributos del formulario
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de usuario'}))
    
    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "email", "is_active", "dni"]
    
    def __init__(self, *args, **kwargs):
        super(FormUser, self).__init__(*args, **kwargs)
        
        add_class_form_control = ["first_name", "last_name", "email", "dni", "password1", "password2"]
        for f in self.fields:
            if f in add_class_form_control:
                self.fields[f].widget.attrs["class"] = "form-control"
        
    def clean_dni(self):
        dni = self.cleaned_data["dni"]
        if not (7 <= len(str(dni)) <= 8):
            raise ValidationError("DNI invalido")
        return dni