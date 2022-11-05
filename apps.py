from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class DemoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demoapp'

    def ready(self):
        import demoapp.signals 
