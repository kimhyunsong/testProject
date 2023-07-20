from django.apps import AppConfig
import threading
import time
from .matches import get_data
def interval_function(interval_seconds):
    while True:
        get_data()
        time.sleep(interval_seconds)
class CricketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cricket'
    
    def ready(self):
        interval_seconds = 300
        timer_thread = threading.Thread(target=interval_function, args=(interval_seconds,))
        timer_thread.daemon = True
        timer_thread.start()
