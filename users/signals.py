from django.db.models.signals import post_save
#import User as sender
from django.contrib.auth.models import User
#import receiver
from django.dispatch import receiver
#we want with each new user a new profile be created.
from .models import Profile

#the signal we are sending is the post_save and the sender is User
#fired anytime there is a User create
#there is the receiver and the receiver is the create_profile
#and it takes all of the arguments that our post_save signal is passing
#which is the instance of the created user and the create function
#now if user is created, then use the instance of that user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
