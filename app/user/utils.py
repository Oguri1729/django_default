

from config.utils import templates_html
from django.conf import settings


def user_html(name):
    return templates_html(settings.USER_APP_NAME, name)
