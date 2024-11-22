from django.views.generic import CreateView, TemplateView
from django.shortcuts import render

class Tela_Login(TemplateView):
    template_name = "Usuarios/Login.html"
    
class Tela_Register(TemplateView):
    template_name = "Usuarios/Register.html"