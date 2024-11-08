from django import forms
from .models import AccountHolder
from django.core.exceptions import ValidationError

class AccountHolderForm(forms.ModelForm):
    class Meta:
        model = AccountHolder
        fields = ['name', 'accountno', 'dob', 'age', 'city', 'phone_number', 'email', 'gender', 'image', 'branch', 'username', 'password', 'initialdeposit']

    def clean_accountno(self):
        accountno = self.cleaned_data.get('accountno')
        if AccountHolder.objects.filter(accountno=accountno).exists():
            raise ValidationError("This account number already exists. Please enter a different one.")
        return accountno


class TransferForm(forms.Form):
    receiver_accountno = forms.CharField(max_length=11, required=True)
    amount = forms.DecimalField(max_digits=12, decimal_places=2, required=True)




from django import forms

class BillPaymentForm(forms.Form):
    biller_name = forms.CharField(max_length=100)
    account_number = forms.CharField(max_length=20)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
