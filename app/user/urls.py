

from django.conf import settings

from django.urls import path

from .views import HomeView
app_name = settings.USER_APP_NAME

urlpatterns = [
    path(
        settings.USER_URL_HOME + '/',
        HomeView.as_view(),
        name='home'
    ),

]
