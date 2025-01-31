from django import forms

from .models import Transaction


class TransactionCreateForm(forms.ModelForm):

    class Meta:
        model = Transaction
        # fields =