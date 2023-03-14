
import uuid
from django.contrib import auth
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
# _ は翻訳してくれる関数だと思っていい
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    '''
    カスタムユーザーに必要らしい
    ユーザー作成時のチェック関係っぽい
    '''
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def with_perm(
            self,
            perm,
            is_active=True,
            include_superusers=True,
            backend=None,
            obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." %
                backend)
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class UserMaster(AbstractBaseUser, PermissionsMixin):
    '''
    ユーザーマスタ
    ID:
        プライマリー
        ユーザーからは確認できない内部ID
    メールアドレス:
        usernameの代わり
        ユニーク設定だがメールアドレス失効後とかの扱いどうすればいいのかな
        CHATGPT
        メールアドレスが共有された場合、別の識別子を使用してユーザーを識別することができます。例えば、ユーザー名、電話番号、またはID番号などが考えられます。
        ユーザーがメールアドレスを変更する場合、アプリケーションは新しいメールアドレスが既に使用されていないかどうかを確認する必要があります。
        アカウントを削除した場合、メールアドレスを再利用する前に一定期間を経過するように設定することができます。
        
    パスワード
        ハッシュ化パスワードかSNSログイントークンが入る
    作成日

    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_superuser = models.BooleanField(_('superuser_status'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # allauthでusernameが必要になるので。
    @property
    def username(self):
        return self.email
