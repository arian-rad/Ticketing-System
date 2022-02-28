from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username,  password=None):
        """
        Creates and saves a User with the given phone_number
        """
        if not username:
            raise ValueError('Users must have an phone_number')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given phone_number
        """
        user = self.create_user(
            username=username,
            password=password
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user
