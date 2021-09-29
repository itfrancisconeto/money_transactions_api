from django.contrib import admin
from money_transactions.models import Transactions

# Register your models here.
class ModelTransactions(admin.ModelAdmin):
    list_display = ('id', 'payer_user', 'receiver_user', 'transferred_value', 'transferred_date')
    list_display_links = ('id', 'payer_user', 'receiver_user')
    search_fields = ('payer_user', 'receiver_user',)
    list_per_page = 20

admin.site.register(Transactions, ModelTransactions)
