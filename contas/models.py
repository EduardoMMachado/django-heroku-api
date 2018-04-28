# -*- coding=utf-8 -*-

# Implemented by Eduardo Machado

from django.db import models
from django.contrib.auth.models import User
import hashlib

class Transaction(models.Model):
    """
        Transaction Model

        Attributes:
            register_name:  The name or short description of transaction.
            amount:         Amount of money of transaction.
    """

    register_name = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        """
            Is a overwritten of the __str__ method to show the register_name when
            print(Transaction.object) is used.
        """

        return self.register_name
