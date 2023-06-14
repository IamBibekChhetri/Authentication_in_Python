from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    # Add your custom fields here
    email = models.EmailField(unique=True)
    additional_field = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, null=False)
    image = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []