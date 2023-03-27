from django import forms
from .models import account



class DetailForm(forms.ModelForm):
    password = forms.IntegerField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = account
        fields = ['Ac_NO', 'password']

class DepositForm(forms.ModelForm):
    amount = forms.DecimalField()
    password = forms.IntegerField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = account
        fields = ['Ac_NO', 'password','amount']

class ChangePasswordForm(forms.ModelForm):
    New_password = forms.IntegerField(label='Password', widget=forms.PasswordInput)
    password = forms.IntegerField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = account
        fields = ['Ac_NO', 'password','New_password']

class WithdrawForm(forms.ModelForm):
    amount = forms.DecimalField()
    password = forms.IntegerField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = account
        fields = ['Ac_NO', 'password','amount']

class DeleteForm(forms.ModelForm):
    password = forms.IntegerField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = account
        fields = ['Ac_NO', 'password']