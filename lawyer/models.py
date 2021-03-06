from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .validators import validate_phone_number, validate_cpf
import re


class Lawyer(models.Model):
    user = models.OneToOneField(
        verbose_name=_("User"),
        to=User,
        help_text=_("It is necessary to relate a user to the Lawyer to access the system.")
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=120
    )
    phone_number = models.CharField(
        verbose_name=_("Phone"),
        max_length=13,
        validators=[validate_phone_number]
    )
    cpf = models.CharField(
        verbose_name=_("CPF"),
        max_length=14,
        unique=True,
        validators=[validate_cpf]
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        unique=True
    )

    class Meta:
        verbose_name = _("Lawyer")
        verbose_name_plural = _("Lawyers")

    def __str__(self):
        return self.name

    def clean(self):
        """Digits only for fields `cpf` and `phone_number`"""
        if self.cpf:
            self.cpf = re.sub('[^0-9]', '', self.cpf)
        if self.phone_number:
            self.phone_number = re.sub('[^0-9]', '', self.phone_number)


class Proposal(models.Model):
    quotation = models.ForeignKey(
        verbose_name=_("Quotation"),
        to='company.Quotation',
        related_name='proposals'
    )
    lawyer = models.ForeignKey(
        verbose_name=_("Lawyer"),
        to=Lawyer,
        related_name='proposals'
    )
    price = models.DecimalField(
        verbose_name=_("Price"),
        max_digits=15,
        decimal_places=2
    )
    created_date = models.DateTimeField(
        verbose_name=_("Created date"),
        auto_now_add=True,
        editable=False
    )

    class Meta:
        verbose_name = _("Proposal")
        verbose_name_plural = _("Proposals")
        unique_together = ['quotation', 'lawyer']
        ordering = ['created_date']

    def __str__(self):
        return "PROP-{:05d}".format(self.pk)
