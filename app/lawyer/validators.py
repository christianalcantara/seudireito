# Author: Christian Douglas <christian.douglas.alcantara@gmail.com>
import re
from django.core.exceptions import ValidationError
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

phone_digits_re = re.compile(r'^(\d{2})[-.]?(\d{4,5})[-.]?(\d{4})$')
cpf_digits_re = re.compile(r'^(\d{3})\.(\d{3})\.(\d{3})-(\d{2})$')


def validate_phone_number(value):
    value = re.sub('(\(|\)|\s+)', '', force_text(value))
    m = phone_digits_re.search(value)
    if not m:
        raise ValidationError(_(
            'Phone numbers must be in either of the '
            'following formats: XX-XXXX-XXXX or XX-XXXXX-XXXX.'
        ))


def dv_maker(v):
    if v >= 2:
        return 11 - v
    return 0


def validate_cpf(value):
    """Value can be either a string in the format XXX.XXX.XXX-XX or an 11-digit number."""

    error_messages = {
        'invalid': _("Invalid CPF number."),
        'max_digits': _("This field requires at most 11 digits or 14 characters."),
    }

    orig_value = value[:]
    if not value.isdigit():
        cpf = cpf_digits_re.search(value)
        if cpf:
            value = ''.join(cpf.groups())
        else:
            raise ValidationError(error_messages['invalid'])

    if len(value) != 11:
        raise ValidationError(error_messages['max_digits'])
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx])
                   for idx, i in enumerate(range(10, 1, -1))])
    new_1dv = dv_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx])
                   for idx, i in enumerate(range(11, 1, -1))])
    new_2dv = dv_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        raise ValidationError(error_messages['invalid'])
    if value.count(value[0]) == 11:
        raise ValidationError(error_messages['invalid'])
    return orig_value
