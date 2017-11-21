from django.contrib import admin
from .models import TypeOfCompany, Company


@admin.register(TypeOfCompany)
class TypeOfCompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_filter = ['type_of_company']
    list_display = ['name', 'type_of_company', 'email']
