from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Subscriber

User = get_user_model()  # Get the User model (especially useful if using a custom user model)

@receiver(post_save, sender=User)
def create_subscriber(sender, instance, created, **kwargs):
    if created:
        # Create a subscriber when a new user is created
        Subscriber.objects.create(user=instance)
        print(f"Subscriber created for user: {instance.username}")
