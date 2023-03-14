from .path import BASE_DIR
# django secret key
SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
INTERNAL_IPS = ['*']
SUPER_ACCOUNT = ''
SUPER_ACCOUNT_PASSWORD = ''
GOOGLE_KEY = ''
GOOGLE_SECRET = ''
