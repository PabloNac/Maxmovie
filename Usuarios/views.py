from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from Usuarios.models import Register

class Tela_Login(TemplateView):
    template_name = "Usuarios/Login.html"
    
class Tela_Register(CreateView):
    model = Register
    fields = ["Usuario", "Email", "Senha"]
    template_name = "Usuarios/Register.html"
    success_url = reverse_lazy("Tela_Login")