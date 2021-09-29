from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator

# Create your models here.
class Transactions(models.Model):
    payer_user = models.CharField(max_length=150)
    receiver_user = models.CharField(max_length=150)
    transferred_value = models.DecimalField(default=0, max_digits=30, decimal_places=2, validators=[MinValueValidator(0)])
    transferred_date = models.DateTimeField(default=datetime.now().replace(microsecond=0), blank=True)