
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from config.views import IndexView
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static


urlpatterns = i18n_patterns(
    path(settings.URL_ADMIN + '/', admin.site.urls),
    path(settings.URL_INDEX, IndexView.as_view(), name='index'),
    path(settings.URL_ALLAUTH, include('allauth.urls')),
    path(settings.USER_URL_INDEX, include(f'{settings.USER_APP_NAME}.urls')),
    prefix_default_language=False
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (
        path('__debug__', include(debug_toolbar.urls)),
    )

