from django.contrib import admin
from django.db import models
from .models import Profile

admin.site.site_header = 'True Value Access LLP'

admin.site.register(Profile)