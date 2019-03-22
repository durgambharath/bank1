from django.db import models


class BankMaster(models.Model):
    bank_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)

    def __str__(self):
        return self.bank_name

