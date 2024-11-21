from django.shortcuts import render


def Tela_login(request):
    return render(request, "Usuarios/Login.html")

def Tela_register(request):
    return render(request, "Usuarios/Register.html")
