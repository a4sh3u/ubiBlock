from django.db import models
from django.db.models import CharField


class CustomerAccounts(models.Model):
    id = models.AutoField(primary_key=True)
    mail_id = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    create_date = models.DateTimeField('date published')
    account_id = models.CharField(max_length=200)
    account_password = models.CharField(max_length=200)
    account_balance = models.CharField(max_length=200)

class Transactions(models.Model):
    txn_id = models.AutoField(primary_key=True)
    txn_hash = models.CharField(max_length=200)
    txn_from_address = models.CharField(max_length=200)
    txn_value = models.CharField(max_length=200)