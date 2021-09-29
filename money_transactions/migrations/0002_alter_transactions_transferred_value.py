# Generated by Django 3.2.6 on 2021-09-23 14:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='transferred_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]