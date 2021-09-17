from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.db import models

from .models import *


@admin.register(DadosArduino)
class DadosArduino(admin.ModelAdmin):
    model = DadosArduino