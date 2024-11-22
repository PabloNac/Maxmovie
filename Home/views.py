from django.views.generic import CreateView, TemplateView
from django.shortcuts import render


class home(TemplateView):
    template_name = "Home/home.html"