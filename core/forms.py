from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    confirmar_contrasena = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombre', 'nombre_usuario', 'email', 'contrasena', 'confirmar_contrasena', 'fecha_nacimiento', 'direccion_despacho']
        widgets = {
            'contrasena': forms.PasswordInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get('contrasena')
        confirmar_contrasena = cleaned_data.get('confirmar_contrasena')

        if contrasena and confirmar_contrasena and contrasena != confirmar_contrasena:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data
    
class LoginForm(forms.Form):
    email = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput)