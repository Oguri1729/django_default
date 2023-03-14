from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from user.models import UserMaster
from django.db import IntegrityError


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        if user.id or not user.email or sociallogin.is_existing:
            return

        try:
            user = UserMaster.objects.get(email=user.email)
        except UserMaster.DoesNotExist:
            pass
        try:
            sociallogin.connect(request, user)
        except IntegrityError:
            from django.contrib import messages
            messages.error(
                request, 'Failed to connect Google account to your account.')
