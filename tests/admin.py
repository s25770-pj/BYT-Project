from django.contrib import admin
from .models import Exercise, ClassRoom

admin.site.register(Exercise, ClassRoom)
