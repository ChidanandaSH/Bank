from django.db import models
from django.core.exceptions import ValidationError

# Custom validator for 10-digit phone number
def validate_10_digits(value):
    if len(str(value)) != 10:
        raise ValidationError('This field must be exactly 10 digits long.')

def validate_11_digits(value):
    if len(str(value)) != 11:
        raise ValidationError('The account number must be exactly 11 digits long.')        

class AccountHolder(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=100)
    
    # No max_length for IntegerField, and use validators for limiting digits
    #accountno = models.BigIntegerField(unique=True, validators=[validate_10_digits])
    accountno = models.CharField(
        max_length=11, 
        unique=True, 
        validators=[validate_11_digits],
        help_text="Enter exactly 11 digits for the account number."
    )


    dob = models.DateField()
    age = models.IntegerField()
    city = models.CharField(max_length=100)

    # Changed to CharField for handling leading zeroes in phone numbers
    phone_number = models.CharField(max_length=10, validators=[validate_10_digits],default='9999999999')
    
    # EmailField for email validation
    email = models.EmailField(max_length=120)
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')
    
    # Image field for uploading photos
    image = models.ImageField(upload_to='Holder_images/')
    
    branch = models.CharField(max_length=20)
    
    # Username should be unique
    username = models.CharField(max_length=150, unique=True)

    # For security, password should be hashed
    password = models.CharField(max_length=128)
    
    initialdeposit = models.FloatField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 

    # Timestamps for tracking updates
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from django.utils import timezone
from django.contrib.auth.models import User  # Assuming you are using Django's built-in User model

class Transaction(models.Model):
    accountno = models.ForeignKey('AccountHolder', on_delete=models.CASCADE)
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    debit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Transaction for {self.accountno} on {self.timestamp}"



class BillPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    biller_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)  # For utility companies
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Pending', 'Pending')])

    def __str__(self):
        return f"{self.biller_name} - {self.account_number}"
























"""from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validate_10_digits(value):
    if len(str(value)) != 10:
        raise ValidationError('This field must be exactly 10 digits long.')

class AccountHolder(models.Model):
    GENDER_CHOICES = [
       ('M', 'Male'),
       ('F', 'Female'),
       ('O', 'Other'),
    ]
    name = models.CharField(max_length=100)
    accountno = models.IntegerField(max_length=11 ,unique=True)
    dob = models.DateField()
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    phone_number = models.BigIntegerField(validators=[validate_10_digits])
    email = models.CharField(max_length=120)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='Holder_images/')
    branch = models.CharField(max_length=20)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    initialdeposit = models.FloatField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


'''class WatchesUploads(models.Model):
    name= models.CharField(max_length=100)  #string, number, decimal
    description = models.TextField()
    price= models.FloatField()
    image= models.ImageField(upload_to='watch_images/')

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)'''"""