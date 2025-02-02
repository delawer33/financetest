from django import forms
from django.utils import timezone

from .models import Transaction


class TransactionCreateForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'value': timezone.now().date()
            }
        )
    )


    def save(self, commit=True):
        trans = super().save(commit=False)
        if commit:
            trans.save()
        return trans

    class Meta:
        model = Transaction
        fields = ('category', 'date', 'type', 'amount', 'description')
