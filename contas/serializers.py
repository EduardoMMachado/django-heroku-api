# -*- coding=utf-8 -*-

# Implemented by Eduardo Machado

from rest_framework import serializers

from .models import Transaction

class GetSerializer(serializers.Serializer):
    """
        List Serializer
    """

    range_start = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    range_end = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)


class TransactionSerializer(serializers.Serializer):
    """
        List Serializer
    """

    register_name = serializers.CharField(required=False)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
