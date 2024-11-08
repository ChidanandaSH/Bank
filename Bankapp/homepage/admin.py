from django.contrib import admin
from .models import AccountHolder, Transaction, BillPayment

@admin.register(AccountHolder)
class AccountHolderAdmin(admin.ModelAdmin):
    list_display = ['name', 'accountno', 'get_balance']  # Update to use the method
    
    def get_balance(self, obj):
        # Assuming that the balance is the latest balance from the Transaction model
        last_transaction = Transaction.objects.filter(accountno=obj).last()
        return last_transaction.balance if last_transaction else 0.00  # Return the balance or 0 if no transactions exist
    get_balance.short_description = 'Balance'  # This will display as "Balance" in the admin panel

# Register BillPayment model
admin.site.register(BillPayment)

# Register Transaction model with TransactionAdmin configuration
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('accountno', 'credit', 'debit', 'balance', 'timestamp')  # Columns to show in the admin panel
    search_fields = ('accountno',)  # Searchable fields in the admin panel
