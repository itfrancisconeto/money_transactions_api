from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from money_transactions.models import Transactions
from money_transactions.serializer import TransactionSerializer

class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]