from rest_framework import serializers
from .models import mobile,CallbackData,SuccesfulTransactions,CancelledTransactions


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = mobile
        fields = '__all__'


class succesfulTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccesfulTransactions
        fields = '__all__'


class cancelledTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CancelledTransactions
        fields = '__all__'


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

    def create(self, validated_data):
        stk_callback_data = validated_data['Body']['stkCallback']

        # Extracting data from CallbackMetadata
        callback_metadata = stk_callback_data.get('CallbackMetadata', {})
        items = callback_metadata.get('Item', [])

        # Creating an instance of the CallbackData model
        callback_data_instance = CallbackData(
            merchant_request_id=stk_callback_data['MerchantRequestID'],
            checkout_request_id=stk_callback_data['CheckoutRequestID'],
            result_code=stk_callback_data['ResultCode'],
            result_desc=stk_callback_data['ResultDesc'],
            amount=self.get_item_value(items, 'Amount'),
            mpesa_receipt_number=self.get_item_value(items, 'MpesaReceiptNumber'),
            balance=self.get_item_value(items, 'Balance'),
            transaction_date=self.get_item_value(items, 'TransactionDate'),
            phone_number=self.get_item_value(items, 'PhoneNumber')
        )

        # Saving the instance to the database
        callback_data_instance.save()

        return callback_data_instance

    def get_item_value(self, items, name):
        for item in items:
            if item.get('Name') == name:
                return item.get('Value')
        return None

