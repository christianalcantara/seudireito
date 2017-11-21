from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class TypeOfCompany(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=120,
        unique=True
    )

    class Meta:
        verbose_name = _("Type of company")
        verbose_name_plural = _("Type of companies")

    def __str__(self):
        return self.name


class Company(models.Model):
    user = models.OneToOneField(
        verbose_name=_("User"),
        to=User,
        help_text=_("It is necessary to relate a user to the Company to access the system.")
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=120
    )
    type_of_company = models.ForeignKey(
        verbose_name=_("Type of company"),
        to=TypeOfCompany,
        null=True,
        on_delete=models.SET_NULL
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        unique=True
    )

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def __str__(self):
        return self.name
