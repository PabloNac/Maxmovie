from django import forms
from Usuarios.models import Register


class Login_Form(forms.ModelForm):
    class Meta:
        model = Register
        fields = ["Nome", "email", "password"]
        widgets = {
            "Nome": forms.TextInput(
                attrs={"placeholder": "Digite seu nome de usuário"}
            ),
            "password": forms.PasswordInput(attrs={"class": "ola"}),
        }
