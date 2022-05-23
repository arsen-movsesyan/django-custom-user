from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from user.managers import UserManager


class User(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta(AbstractBaseUser.Meta):
        swappable = 'AUTH_USER_MODEL'
