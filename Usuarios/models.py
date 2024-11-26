from django.db import models

##Refatorando Login para Register
class Register(models.Model):
    __name__="Register"
    Usuario = models.CharField(max_length=50, null=False, blank=False)
    Email = models.EmailField(max_length=254, null=False, blank=False)
    Senha = models.CharField(max_length=50, null=False, blank=False)
 