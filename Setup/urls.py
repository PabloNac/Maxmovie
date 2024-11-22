from django.contrib import admin
from django.urls import path

from Home.views import home
from Usuarios.views import Tela_Login, Tela_Register

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home.as_view(), name="home"),
    path("Login/", Tela_Login.as_view(), name="Tela_Login"),
    path("Registrar-se/", Tela_Register.as_view(), name="Tela_Register"),
]
