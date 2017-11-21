from django import forms
from .models import Company
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from app.lawyer.forms import LawyerCreationForm


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
