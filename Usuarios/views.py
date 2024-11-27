from django.views.generic import CreateView, TemplateView, FormView
from django.urls import reverse_lazy
from Usuarios.models import Register
from Usuarios.forms import Login_Form

class Tela_Login(FormView):
    form_class = Login_Form
    template_name = "Usuarios/Login.html"
    
    def form_valid(self, form):
        
        username = form.cleaned_data['Usuario']
        
        form.save()
        return super().form_valid(form)
    
class Tela_Register(CreateView):
    model = Register
    form_class = Login_Form

    template_name = "Usuarios/Register.html"
    success_url = reverse_lazy("Tela_Login")
    
    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)