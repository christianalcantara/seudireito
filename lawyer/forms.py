from django import forms
from .models import Lawyer
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.models import User


class LawyerCreationForm(forms.ModelForm):
    """
    A form that creates a lawyer and related user with no privileges, from the given
    email and password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'user_exists': _("A user with that email already exists.")
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = Lawyer
        exclude = ['user']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_exists = User.objects.filter(username=email).exists()
        if user_exists:
            raise forms.ValidationError(
                self.error_messages['user_exists'],
                code='user_exists',
            )
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        self.instance.username = self.cleaned_data.get('username')
        password_validation.validate_password(password1)
        return password2

    def save(self, commit=True):
        lawyer = super(LawyerCreationForm, self).save(commit=False)
        if commit:
            user = User.objects.create_user(
                username=self.cleaned_data.get("email"),
                email=self.cleaned_data.get("email"),
                password=self.cleaned_data.get("password1"),
                first_name=self.cleaned_data.get("name")
            )
            lawyer.user = user
            lawyer.save()
        return lawyer
