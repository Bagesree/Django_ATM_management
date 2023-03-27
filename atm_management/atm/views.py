from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db.models import F
from decimal import Decimal
from datetime import datetime
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView
from .form import DepositForm, ChangePasswordForm, WithdrawForm, DeleteForm, DetailForm
from .models import account,Transaction
from django.contrib.auth.decorators import login_required
from django.core.validators import RegexValidator
from django.db.models import Q
from django.core.exceptions import ValidationError

@login_required(login_url='/login/')
def main(request):
    send_mail(
        'Subject',
        'Message.',
        'dummydjango3@gmail.com',
        ['bagesree27@gmail.com'],
    )
    return render(request,'main.html')

class Newaccount(CreateView):
    model = account
    fields = ['IFSC','Ac_NO', 'Ac_type','password']
    success_url = reverse_lazy('login')
    template_name = 'newaccount.html'


@login_required(login_url='/login/')
def details(request):

    if request.method == 'POST':
        form = DetailForm(request.POST)
        # Handle the user input data

        Ac_NO = request.POST.get('Ac_NO')
        password = request.POST.get('password')

        ac_no_validator = RegexValidator(regex=r'^\d{8}$', message='Account number must be 8 digits')

        try:
            ac_no_validator(Ac_NO)
        except ValidationError as e:
            form.add_error('Ac_NO', e.message)

        password_validator = RegexValidator(regex=r'^\d{6}$', message='Account number must be 6 digits')

        try:
            password_validator(password)
        except ValidationError as e:
            form.add_error('password', e.message)

        user = account.objects.filter(Ac_NO=Ac_NO, password=password).first()
        if user:

            my_objects = account.objects.filter(Ac_NO=Ac_NO)
            return render(request,'accontdetails.html',{'my_objects': my_objects})
        else:
            # If no matching record is found, return an error message
            error_msg = "Invalid AC_NO or password"
            return render(request, 'details.html', {'form': form, 'error_msg': error_msg})
    else:
        form = DetailForm()
    return render(request,'details.html',{'form': form})


@login_required(login_url='login')
def deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        Ac_NO = request.POST.get('Ac_NO')
        password = request.POST.get('password')
        Amount = request.POST.get('amount')

        ac_no_validator = RegexValidator(regex=r'^\d{8}$', message='Account number must be 8 digits')

        try:
            ac_no_validator(Ac_NO)
        except ValidationError as e:
            form.add_error('Ac_NO', e.message)

        password_validator = RegexValidator(regex=r'^\d{6}$', message='Account number must be 6 digits')

        try:
            password_validator(password)
        except ValidationError as e:
            form.add_error('password', e.message)

        user = account.objects.filter(Ac_NO=Ac_NO, password=password).first()
        if user is not None and Amount is not None:
            amount_decimal = Decimal(Amount)
            account.objects.filter(Ac_NO=Ac_NO).update(Balance=F('Balance') + amount_decimal)
            w = Transaction(Ac_NO=Ac_NO, Credit=Amount, Date_and_time=timezone.now(), Debit=0,Balance=user.Balance + amount_decimal)
            w.save()


            return redirect('main')
        else:
            error_msg = "Invalid AC_NO or password"
            return render(request, 'deposite.html', {'form': form, 'error_msg': error_msg})
    else:
        form = DepositForm()
    return render(request, 'deposite.html', {'form': form})


@login_required(login_url='login')
def change_password(request):

    form = ChangePasswordForm(request.POST)
    if request.method == 'POST':

        Ac_NO = request.POST.get('Ac_NO')
        password = request.POST.get('password')
        New_password = request.POST.get('New_password')

        ac_no_validator = RegexValidator(regex=r'^\d{8}$', message='Account number must be 8 digits')

        try:
            ac_no_validator(Ac_NO)
        except ValidationError as e:
            form.add_error('Ac_NO', e.message)

        password_validator = RegexValidator(regex=r'^\d{6}$', message='Account number must be 6 digits')

        try:
            password_validator(password)
        except ValidationError as e:
            form.add_error('password', e.message)
        user = account.objects.filter(Ac_NO=Ac_NO, password=password).first()
        if user:
            print(user)
            if New_password is not None:
                account.objects.filter(Ac_NO=Ac_NO).update(password=New_password)

                # transaction = Transaction.objects.create(account=account, amount=amount)
                return redirect('main')
        else:
            error_msg = "Invalid AC_NO or password"
            return render(request,'password.html',{'form': form, 'error_msg': error_msg})
    else:
        form = ChangePasswordForm()
    return render(request, 'password.html', {'account': account, 'form': form})


@login_required(login_url='login')
def withdraw(request):
    form = WithdrawForm(request.POST)
    if request.method == 'POST':

        Ac_NO = request.POST.get('Ac_NO')
        password = request.POST.get('password')
        Amount = request.POST.get('amount')

        ac_no_validator = RegexValidator(regex=r'^\d{8}$', message='Account number must be 8 digits')

        try:
            ac_no_validator(Ac_NO)
        except ValidationError as e:
            form.add_error('Ac_NO', e.message)

        password_validator = RegexValidator(regex=r'^\d{6}$', message='Account number must be 6 digits')

        try:
            password_validator(password)
        except ValidationError as e:
            form.add_error('password', e.message)


        user = account.objects.filter(Ac_NO=Ac_NO,password=password).first()
        if user is not None and Amount is not None:
            amount_decimal = Decimal(Amount)
            if amount_decimal <= user.Balance:
                account.objects.filter(Ac_NO=Ac_NO).update(Balance=F('Balance') - amount_decimal)
                w=Transaction(Ac_NO=Ac_NO,Debit=Amount,Date_and_time=timezone.now(),Credit=0,Balance=user.Balance - amount_decimal)
                w.save()



                return redirect('main')
            else:
                error_msg = "Insufficient balance"
                return render(request, 'withdraw.html', {'form': form, 'error_msg': error_msg})
        else:
            error_msg = "Invalid AC_NO or password"
            form.fields['Ac_NO'].validators.append(ac_no_validator)
            form.fields['password'].validators.append(password_validator)
            return render(request, 'withdraw.html', {'form': form, 'error_msg': error_msg})
    else:
        form = WithdrawForm()
    return render(request, 'Withdraw.html', {'form': form})

@login_required(login_url='login')
def delete_account(request):
    form = DeleteForm(request.POST)
    if request.method == 'POST':
        Ac_NO = request.POST.get('Ac_NO')
        password = request.POST.get('password')

        ac_no_validator = RegexValidator(regex=r'^\d{8}$', message='Account number must be 8 digits')

        try:
            ac_no_validator(Ac_NO)
        except ValidationError as e:
            form.add_error('Ac_NO', e.message)

        password_validator = RegexValidator(regex=r'^\d{6}$', message='Account number must be 6 digits')

        try:
            password_validator(password)
        except ValidationError as e:
            form.add_error('password', e.message)

        user = account.objects.filter(Ac_NO=Ac_NO, password=password).first()
        if user is not None:
            user.delete()
            return redirect('main')
        else:
            error_msg = "Invalid AC_NO or password"
            return render(request, 'delete.html', {'form': form, 'error_msg': error_msg})
    else:
        form = DeleteForm()
    return render(request, 'delete.html', {'form': form})

@login_required(login_url='login')
def transaction(request):

    transactions = Transaction.objects.all()
    return render(request, 'Transaction.html', {'transactions': transactions})


class SearchResultView(ListView):
    model = Transaction
    template_name = 'search.html'

    def get_queryset(self):
        query =self.request.GET.get('q')
        return Transaction.objects.filter(Q(Debit=query)|Q(Credit=query))



def contact(request):
    return render(request,'contact.html')


