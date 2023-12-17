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


class cancelledTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = cancelledTransactions
        fields = '__all__'