from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import AccountHolder,Transaction
from .forms import AccountHolderForm,TransferForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



def signup(request):
    if request.method == 'POST':
        form = AccountHolderForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a user with password hashing
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            # Save AccountHolder model fields and associate with the user
            account_holder = form.save(commit=False)
            account_holder.user = user  # Associate the user with the account holder
            account_holder.save()

            messages.success(request, 'Account created successfully!')
            return render(request, 'home.html')  # Redirect to home or dashboard
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AccountHolderForm()

    return render(request, 'signup.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Get username and password from form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate the user using Django's built-in authenticate method
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # If the user is authenticated, log the user in
                login(request, user)
                return redirect('home')  # Redirect to home or any other page after login
            else:
                # Authentication failed
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to login page or any other page after logout


@login_required(login_url="/login")
def transaction_history(request):
    # Get the account holder associated with the logged-in user
    account_holder = AccountHolder.objects.get(username=request.user.username)
    
    # Get all transactions for this account holder
    transactions = Transaction.objects.filter(accountno=account_holder).order_by('-timestamp')

    return render(request, 'transaction_history.html', {'transactions': transactions})




from django.db import transaction
# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .forms import TransferForm
from .models import AccountHolder, Transaction
@login_required
def transfer_view(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            # Get the sender's account using the logged-in user
            sender = AccountHolder.objects.get(username=request.user.username)  # Use username to fetch AccountHolder
            
            # Receiver's account number and transfer amount from form
            receiver_accountno = form.cleaned_data.get('receiver_accountno')
            amount = form.cleaned_data.get('amount')

            try:
                # Fetch receiver account using the provided account number
                receiver = AccountHolder.objects.get(accountno=receiver_accountno)

                # Ensure the sender has sufficient balance
                if sender.balance < amount:
                    messages.error(request, "Insufficient balance for the transfer.")
                    return redirect('transfer')

                # Begin the atomic transaction block to ensure both debit and credit happen together
                with transaction.atomic():
                    # Debit sender account
                    sender.balance -= amount
                    sender.save()

                    # Credit receiver account
                    receiver.balance += amount
                    receiver.save()

                    # Log the sender's transaction (debit)
                    Transaction.objects.create(
                        accountno=sender,
                        debit=amount,
                        balance=sender.balance
                    )

                    # Log the receiver's transaction (credit)
                    Transaction.objects.create(
                        accountno=receiver,
                        credit=amount,
                        balance=receiver.balance
                    )

                # Success message on successful transfer
                messages.success(request, "Transfer completed successfully!")
                return redirect('transaction_history')

            except AccountHolder.DoesNotExist:
                # If the receiver account number doesn't exist
                messages.error(request, "Receiver account does not exist.")
                return redirect('transfer')

    else:
        form = TransferForm()

    return render(request, 'transfer.html', {'form': form})






from .models import BillPayment
from .forms import BillPaymentForm
from django.utils import timezone
from datetime import timedelta

@login_required(login_url="/login")
def bill_payment_view(request):
    if request.method == 'POST':
        form = BillPaymentForm(request.POST)
        if form.is_valid():
            BillPayment.objects.create(
                user=request.user,
                biller_name=form.cleaned_data.get('biller_name'),
                account_number=form.cleaned_data.get('account_number'),
                amount=form.cleaned_data.get('amount'),
                due_date=form.cleaned_data.get('due_date') or timezone.now() + timedelta(days=30),  # Set due_date
                status='Paid'
            )
            messages.success(request, 'Bill paid successfully.')
            return redirect('bill_payment_history')
    else:
        form = BillPaymentForm()

    return render(request, 'bill_payment.html', {'form': form})



@login_required(login_url="/login")
def bill_payment_history(request):
    payments = BillPayment.objects.filter(user=request.user)
    return render(request, 'bill_payment_history.html', {'payments': payments})



# Create your views here.
def home(request):
    return render(request, 'home.html')
  #  return HttpResponse("hi")

from datetime import datetime

def about(request):
    context = {
        'year': datetime.now().year  # Adding the current year for the footer
    }
    return render(request, 'about.html', context)
def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')  # Replace with the correct template path