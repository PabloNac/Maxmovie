from django import forms
from Usuarios.models import Register


class Login_Form(forms.ModelForm):
    class Meta:
        model = Register
        fields = ["Email", "Senha"]
