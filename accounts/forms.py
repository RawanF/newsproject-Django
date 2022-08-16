from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.utils.translation import ugettext_lazy as _


class UserCreationForm(UserCreationForm):
    dob = forms.DateField(label=_('Date of birth'),
                          widget=forms.DateInput(attrs=dict(type='date')))

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone_number",
                  "national_id", "dob", "password1", "password2")
