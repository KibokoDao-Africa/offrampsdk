from rest_framework import serializers
from .models import mobile,succesfulTransactions,cancelledTransactions


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = mobile
        fields = '__all__'


# class succesfulTransactionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = succesfulTransactions
#         fields = '__all__'


# class cancelledTransactionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = cancelledTransactions
#         fields = '__all__'


class CallbackMetadataItemSerializer(serializers.Serializer):
    Name = serializers.CharField()
    Value = serializers.CharField()

class CallbackMetadataSerializer(serializers.Serializer):
    Item = CallbackMetadataItemSerializer(many=True, allow_empty=True)

class StkCallbackSerializer(serializers.Serializer):
    MerchantRequestID = serializers.CharField()
    CheckoutRequestID = serializers.CharField()
    ResultCode = serializers.IntegerField()
    ResultDesc = serializers.CharField()
    CallbackMetadata = CallbackMetadataSerializer(allow_null=True)

class CallbackResponseSerializer(serializers.Serializer):
    Body = serializers.DictField(child=serializers.DictField())
