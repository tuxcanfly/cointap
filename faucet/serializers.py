from rest_framework import serializers
from faucet.models import Transaction


class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    address = serializers.CharField(max_length=64)
    amount = serializers.IntegerField(required=False)
    status = serializers.CharField(required=False, source='get_status_display')
    tx = serializers.CharField(required=False, allow_blank=True, max_length=64)

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.tx = validated_data.get('tx', instance.tx)
        instance.save()
        return instance
