from django import forms

from .models import Transaction


class TransactionCreateForm(forms.ModelForm):

    def save(self, commit=True):
        trans = super().save(commit=False)
        if commit:
            trans.save()
        return trans

    class Meta:
        model = Transaction
        fields = ('category', 'type', 'amount', 'description')
