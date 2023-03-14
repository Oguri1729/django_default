from .user import USER_URL_HOME
URL_ALLAUTH = ''

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # ユーザ登録確認メールを送信する
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/'  # ログアウトリダイレクトの設定
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
AUTH_USER_MODEL = 'user.UserMaster'
LOGIN_REDIRECT_URL = '/' + USER_URL_HOME   # ログインURLの設定
LOGIN_URL = '/login'  # ログイン画面を何処にするかの設定
SITE_ID = 1  # django-allauthを利用する際に必要な設定
SOCIALACCOUNT_ADAPTER = 'user.adapter.SocialAccountAdapter'
# ソーシャルログイン確認画面を使うかどうか
SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'AUTH_PARAMS': {
            'prompt': 'select_account',
            'access_type': 'offline',
        },
        'SCOPE': [
            'profile',
            'email',
        ],

    }, }
SOCIALACCOUNT_STORE_TOKENS = True
