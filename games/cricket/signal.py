from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Events

@receiver( post_save, sender = Events )
def events_post_save( sender, **kwargs ):
    pass