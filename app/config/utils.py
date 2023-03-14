from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.providers.google.provider import GoogleProvider
from django.conf import settings
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from user.models import  UserMaster




@receiver(post_migrate)
def init_db(sender, **kwargs):
    if sender.name == settings.USER_APP_NAME:
        # for s in STATUS_DICT:
        #     Status.objects.get_or_create(name=STATUS_DICT[s], status=s)
        if not UserMaster.objects.filter(email=settings.SUPER_ACCOUNT):
            UserMaster.objects.create_superuser(
                email=settings.SUPER_ACCOUNT,
                password=settings.SUPER_ACCOUNT_PASSWORD)
        # SocialApp.sitesでサイト登録をしないといけない現状手動
        SocialApp.objects.get_or_create(
            provider=GoogleProvider.id,
            name=GoogleProvider.name,
            client_id=settings.GOOGLE_KEY,
            secret=settings.GOOGLE_SECRET,
        )
def connect(sequence, *args):
    return sequence.join(args)

def templates_html(base_path, name):
    return f'{base_path}/{name}.html'
