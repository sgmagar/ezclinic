from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth import (authenticate, get_user_model,
                                 password_validation)
from django.contrib.auth.forms import PasswordResetForm

from djangae.utils import get_in_batches

from . import models as m


class PersonForm(forms.ModelForm):
    pictures = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'required': False, 'multiple': True, 'class': 'form-control'}), required=False)
    time = forms.TimeField(input_formats=["%I:%M %p"])

    class Meta:
        model = m.Person
        fields = ['name', 'last_name', 'age', 'martial_status', 'mobile', 'sex',
                  'amount_paid', 'amount_left', 'note', 'address', 'date', 'time',
                  'treatment_done', 'treatment_plan', 'chief_complain',
                   'dental_chart_type', 'dental_chart']
        widgets = {
            'name': forms.TextInput(attrs={'required': True, 'class': 'form-control',
                                           'placeholder': 'name'}),
            'last_name': forms.TextInput(attrs={'required': True, 'class': 'form-control',
                                                'placeholder': 'lastname'}),
            'age': forms.TextInput(attrs={'required': False, 'class': 'form-control',
                                          'placeholder': 'age'}),
            'amount_paid': forms.TextInput(attrs={'required': False, 'class': 'form-control',
                                                  'placeholder': 'amount paid'}),
            'amount_left': forms.TextInput(attrs={'required': False, 'class': 'form-control',
                                                  'placeholder': 'amount left'}),
            'note': forms.Textarea(attrs={'required': False, 'class': 'form-control',
                                           'placeholder': 'Patient History',
                                           'rows': '3'}),
            'address': forms.TextInput(attrs={'required': False, 'class': 'form-control',
                                              'placeholder': 'Current address'}),
            'chief_complain': forms.TextInput(attrs={'required': False, 'class': 'form-control',
                                                     'placeholder': 'chief complain'}),
            'treatment_plan': forms.Textarea(attrs={'required': False, 'class': 'form-control',
                                                    'placeholder': 'treatment plan', 'rows': '3'}),
            'treatment_done': forms.Textarea(attrs={'required': False, 'class': 'form-control',
                                                    'placeholder': 'treatment done', 'rows': '3'}),
            'dental_chart_type': forms.RadioSelect(),
            'dental_chart': forms.HiddenInput(),


        }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = m.User
        fields = ['username', 'email', 'password', 'country',
                  'last_name', 'first_name', 'city', 'clinic']


class EventForm(forms.ModelForm):
    class Meta:
        model = m.Event
        fields = ['text', 'date']


class AppointmentForm(forms.Form):
    date = forms.DateField()
    time = forms.TimeField(input_formats=["%I:%M %p"], required=False)


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = m.Receipt
        fields = ['amount']


class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    new_password = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        password = self.cleaned_data["new_password"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class AppEnginePasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254)

    def get_users(self, email):
        """Given an email, return matching user(s) who should receive a reset.

        This allows subclasses to more easily customize the default policies
        that prevent inactive users and users with unusable passwords from
        resetting their password.
        """
        active_users = list(get_user_model()._default_manager.filter(
            email__iexact=email, is_active=True))
        # Mild data migration
        # To use __iexact we have to resave models. Djangae do the rest
        # https://djangae.readthedocs.io/en/latest/db_backend/#special-indexes
        if len(active_users) == 0:
            for u in get_in_batches(
                    get_user_model()._default_manager.all(), 30):
                u.save()
            active_users = list(get_user_model()._default_manager.filter(
                email__iexact=email, is_active=True))

        return (u for u in active_users if u.has_usable_password())
