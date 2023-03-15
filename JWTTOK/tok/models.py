from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin, AbstractUser,AbstractBaseUser
# Create your models here.
class MyUser(AbstractBaseUser):
    username = None

    email = models.EmailField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    c_password = models.CharField(max_length=20)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    

