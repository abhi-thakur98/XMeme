from django.contrib import admin
from .models import Owner, Meme
# Register your models here.

admin.site.register([Owner, Meme])