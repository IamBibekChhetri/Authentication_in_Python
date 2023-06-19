import profile
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.files.storage import default_storage
from django.conf import settings


class CustomUser(AbstractUser):
    # Add your custom fields here
    # username = None
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=100,default="")
    phone = models.CharField(max_length=10, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="authentication/image/")

    @receiver(pre_save, sender=profile)
    def delete_old_image(sender, instance, **kwargs):
        if instance.pk:
            try:
                old_instance = sender.objects.get(pk=instance.pk)
                if old_instance.image and old_instance.image != instance.image:
                    # Delete the old image file from storage
                    if old_instance.image.name != "":
                        default_storage.delete(old_instance.image.name)
            except sender.DoesNotExist:
                pass
    
    