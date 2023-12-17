from django.db import models

# Create your models here.
class mobile(models.Model):
    amount = models.DecimalField(decimal_places=2,max_digits=11,default=1)
    mobile_number = models.CharField(max_length=12)

class succesfulTransactions(models.Model):
    MerchantRequestID = models.CharField(max_length=255,)
    CheckoutRequestID = models.CharField(max_length=255,)
    ResultDesc = models.CharField(max_length=255)
    Amount = models.DecimalField(decimal_places=2,max_digits=10)
    MpesaReceiptNumber = models.CharField(max_length=255)
    TransactionDate  = models.DateTimeField(auto_now_add=True)
    PhoneNumber = models.CharField(max_length=30,)

class cancelledTransactions(models.Model):
    MerchantRequestID = models.CharField(max_length=255,)
    CheckoutRequestID = models.CharField(max_length=255,)
    ResultCode = models.CharField(max_length=255)
    