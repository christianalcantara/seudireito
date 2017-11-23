from django.contrib import admin
from .models import Lawyer, Proposal


@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'cpf']


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_filter = ['quotation', 'lawyer', 'created_date']
    list_display = ['quotation', 'lawyer', 'price', 'created_date']
