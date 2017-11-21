from django.contrib import admin
from .models import Lawyer


@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    pass
