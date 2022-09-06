from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user(created, **kwargs):
    instance = kwargs['instance']
    if created:
        print(f'User {instance} is created')
    else:
        print(f'User {instance} is updated')