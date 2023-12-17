from rest_framework import serializers
from .models import mobile,succesfulTransactions,cancelledTransactions


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = mobile
        fields = '__all__'


class succesfulTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = succesfulTransactions
        fields = '__all__'


class cancelledTransactionsSerializer(serializers.Serializer):
    MerchantRequestID = serializers.CharField(max_length=255)
    CheckoutRequestID = serializers.CharField(max_length=255)
    ResultDesc = serializers.CharField(max_length=255)