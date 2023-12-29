from django.forms import forms

from message.models import Mailings


class MailingListForm(forms.Form):
    model = Mailings
    fields = '__all__'