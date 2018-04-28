# -*- coding=utf-8 -*-

# Implemented by Eduardo Machado

from rest_framework import generics, status, exceptions, views
from rest_framework.response import Response

from .models import Transaction
from .serializers import TransactionSerializer, GetSerializer


class TransactionView(views.APIView):
    """
    Transaction View

    Attributes:
        serializer_class: The serializer used for API's responses.
    """

    serializer_class = GetSerializer
    http_method_names = ['get', 'post', 'options']

    def get(self, request, format=None):
        """
            GET

            get list of transactions
        """

        serializer = self.serializer_class(data=request.GET)

        if serializer.is_valid():
            return Response(
                TransactionSerializer(
                    Transaction.objects.all().filter(
                        amount__gt=serializer.data.get('range_start'),
                        amount__lt=serializer.data.get('range_end')
                    ),
                    many=True
                ).data,
                status=status.HTTP_200_OK   
            )


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
