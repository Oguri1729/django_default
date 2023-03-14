from django.apps import AppConfig
from django.conf import settings

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = settings.USER_APP_NAME
