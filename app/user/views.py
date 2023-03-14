from config.utils import templates_html
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
#from user.form import ProfileForm
from user.models import UserMaster
from user.utils import user_html


class HomeView(TemplateView):
    template_name = user_html('home')
