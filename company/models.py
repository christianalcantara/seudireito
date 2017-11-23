from django.contrib.auth.models import User
from django.db import models
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


class Quotation(models.Model):
    company = models.ForeignKey(
        verbose_name=_("Company"),
        to=Company,
        related_name='quotations'
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=150
    )
    description = models.TextField(
        verbose_name=_("Description")
    )
    state = models.CharField(
        verbose_name=_("State"),
        max_length=8,
        choices=[
            ('created', _("Created")),
            ('delegate', _("Delegate")),
            ('finished', _("Finished"))
        ],
        default='created'
    )
    created_date = models.DateTimeField(
        verbose_name=_("Created date"),
        auto_now_add=True,
        editable=False
    )
    delegated_to = models.OneToOneField(
        verbose_name="Delegated to",
        to='lawyer.Proposal',
        blank=True,
        null=True,
        related_name="delegateds"
    )

    class Meta:
        verbose_name = _("Quotation")
        verbose_name_plural = _("Quotations")
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    @property
    def state_color(self):
        colors = {
            'created': 'warning',
            'delegate': 'info',
            'finished': 'success'
        }
        return colors.get(self.state, 'danger')
