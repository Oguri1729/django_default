
from pathlib import Path

# project path
BASE_DIR = Path(__file__).resolve().parent.parent.parent

TEMPLATE_DIR_NAME = 'templates'
STATIC_DIR_NAME = 'static'
MEDIA_DIR_NAME = 'media'
LOCALE_DIR_NAME = 'locale'
# template
TEMPLATE_DIR = BASE_DIR / TEMPLATE_DIR_NAME

# static
STATIC_DIR = BASE_DIR / STATIC_DIR_NAME
STATICFILES_DIRS = [STATIC_DIR]
STATIC_URL = STATIC_DIR_NAME + '/'

# media
MEDIA_DIR = BASE_DIR / MEDIA_DIR_NAME
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = MEDIA_DIR_NAME + '/'

# locale
LOCALE_PATHS = [BASE_DIR / LOCALE_DIR_NAME]
