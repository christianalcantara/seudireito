from django.contrib import admin
from .models import TypeOfCompany, Company, Quotation


@admin.register(TypeOfCompany)
class TypeOfCompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_filter = ['type_of_company']
    list_display = ['name', 'type_of_company', 'email']


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_filter = ['company', 'state', 'delegated_to']
    list_display = ['title', 'company', 'state', 'delegated_to', 'created_date']
