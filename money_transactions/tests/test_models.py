from django.test import TestCase
from money_transactions.models import Transactions

class TransactionsModelTestCase(TestCase):

    def setUp(self):
        self.transactions = Transactions(
            payer_user = 'john',
            receiver_user = 'mary',
            transferred_value = '400.50'
        )

    def test_check_attributes(self):
        """Test for check attributes with default values """
        self.assertEqual(self.transactions.payer_user, 'john')
        self.assertEqual(self.transactions.receiver_user, 'mary')
        self.assertEqual(self.transactions.transferred_value, '400.50')




