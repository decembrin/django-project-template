from django import forms
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from registration.forms import RegistrationForm

from .models import User

TOS_LABEL = 'Я прочитал и согласен с Условиями использования'


class AccountRegistrationForm(RegistrationForm):
    first_name = forms.CharField(label=capfirst(_('first name')), strip=True)
    last_name = forms.CharField(label=capfirst(_('last name')), strip=True)
    tos = forms.BooleanField(
        label=TOS_LABEL,
        required=True,
        error_messages={
            'required': 'Подтвердите согласие с Условиями использования'
        })

    class Meta(object):
        model = User
        fields = ('first_name', 'last_name', 'email', 'tos')
