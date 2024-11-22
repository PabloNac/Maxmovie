from django.contrib import admin
from django.urls import path

from Home.views import home
from Usuarios.views import Tela_login, Tela_register

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("Login/", Tela_login, name="Tela_Login"),
    path("Registrar-se/", Tela_register, nome="Tela_Register"),
]
