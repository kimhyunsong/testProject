from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Events

@receiver( post_save, sender = Events )
def events_post_save( sender, **kwargs ):
    # 시그널로 자고있는 쓰레드에 알려줄 용도
    pass