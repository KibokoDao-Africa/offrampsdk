from django.db import models

# Create your models here.
class mobile(models.Model):
    amount = models.DecimalField(decimal_places=2,max_digits=11,default=1)
    mobile_number = models.CharField(max_length=12)

class SuccesfulTransactions(models.Model):
    MerchantRequestID = models.CharField(max_length=255,)
    CheckoutRequestID = models.CharField(max_length=255,)
    ResultDesc = models.CharField(max_length=255)
    Amount = models.DecimalField(decimal_places=2,max_digits=10)
    MpesaReceiptNumber = models.CharField(max_length=255)
    TransactionDate  = models.DateTimeField(auto_now_add=True)
    PhoneNumber = models.CharField(max_length=30,)

class CancelledTransactions(models.Model):
    MerchantRequestID = models.CharField(max_length=255,)
    CheckoutRequestID = models.CharField(max_length=255,)
    ResultCode = models.CharField(max_length=255)
    
class CallbackData(models.Model):
    merchant_request_id = models.CharField(max_length=255)
    checkout_request_id = models.CharField(max_length=255)
    result_code = models.IntegerField()
    result_desc = models.CharField(max_length=255)
    amount = models.FloatField(null=True)
    mpesa_receipt_number = models.CharField(max_length=255, null=True)
    balance = models.FloatField(null=True)
    transaction_date = models.DateTimeField(null=True)
    phone_number = models.CharField(max_length=15, null=True)

