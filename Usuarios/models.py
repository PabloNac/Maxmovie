from django.db import models
from django.contrib.auth.models import AbstractUser

class Register(AbstractUser):
    
    Nome = models.CharField(max_length=50, null=False, blank=False, unique=True)
    
        
    USERNAME_FIELD = "Nome"
    REQUIRED_FIELDS = ["username"]
    