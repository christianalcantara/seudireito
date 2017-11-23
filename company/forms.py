from django import forms
from django.contrib.auth.models import User

from lawyer.forms import LawyerCreationForm
from .models import Company, Quotation


class CompanyCreationForm(LawyerCreationForm):
    """
    A form that creates a company and related user with no privileges, from the given
    email and password.
    """

    class Meta:
        model = Company
        exclude = ['user']

    def save(self, commit=True):
        company = super(CompanyCreationForm, self).save(commit=False)
        if commit:
            user = User.objects.create_user(
                username=self.cleaned_data.get("email"),
                email=self.cleaned_data.get("email"),
                password=self.cleaned_data.get("password1"),
                first_name=self.cleaned_data.get("name")
            )
            company.user = user
            company.save()
        return company


class QuotationCreateForm(forms.ModelForm):
    """
    A form that create a quotations
    """
    class Meta:
        model = Quotation
        exclude = ['company', 'state', 'created_date']