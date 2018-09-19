from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from faucet.serializers import TransactionSerializer
from faucet.rpc import WalletClient

@api_view(['GET'])
def balance(request):
    balance = WalletClient.get_balance()
    return Response({'balance': balance}, status=status.HTTP_200_OK)

@api_view(['POST'])
def send(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
