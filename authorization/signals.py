from django.contrib.auth.models import User
from .models import Link
from django.db.models.signals import post_save
from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def create_link(sender, instance, created, **kwargs):
#     if created:
#         Link.objects.create(user=instance)