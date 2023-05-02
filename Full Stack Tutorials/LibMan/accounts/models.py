from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from . managers import CustomUserManager

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    sponsored_by = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Borrowed(models.Model):
    user = models.OneToOneField(Member, on_delete=models.CASCADE)
    book = models.OneToOneField(Books, on_delete=models.CASCADE)



class Member(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email_address"), unique=True)
    name  = models.CharField(max_length=100)
    member_from = models.DateField(auto_now_add=True)
    borrowed_books = models.ForeignKey(Borrowed, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.name
    
