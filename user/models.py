from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver


class User(AbstractUser):
    phone = models.CharField(max_length=15, verbose_name="User phone number")
    country = models.CharField(max_length=50, verbose_name="Country by user")

    class Meta:
        db_table = "users" 
        verbose_name = "User"

    def __str__(self):
        return self.username + f"({self.country})"

@receiver(pre_save, sender=User)
def hash_password(sender, instance, **kwargs):
    if (instance.id is None) or (
            sender.objects.get(id=instance.id).password != instance.password
    ):
        instance.set_password(instance.password)