from django.db import models
from django.db.models import CharField


class CustomerAccounts(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    account_id = models.CharField(max_length=200)
    account_password = models.CharField(max_length=200)
    account_balance = models.CharField(max_length=200)
