from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = PhoneNumberField('شماره تلفن همراه', unique=True)
    avatar = models.ImageField(max_length=250, null=True, blank=True, upload_to='avatars/%Y/%m/%d')
    birthdate = models.DateTimeField(verbose_name='تاریخ تولد', null=True, blank=True,)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.username)