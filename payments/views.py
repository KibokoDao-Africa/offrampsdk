
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.api_auth import get_access_token
from django.conf import settings
from .serializers import MobileSerializer, BusinessToCustomerSerializer, StkPushSerializer,DonateSerializer
from .models import SuccesfulTransactions, CancelledTransactions, BusinessToCustomer, Donations
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import requests,json, uuid, base64,datetime, logging, random, string

def encrypt_data(data, key, iv):
    backend = default_backend()

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(data) + encryptor.finalize()

    return ciphertext

# Create your views here.
class ConvertToFiat(APIView):
    serializer_class = MobileSerializer
   

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        access_token = get_access_token()
        print("access token", access_token)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
            }
        if not serializer.is_valid():
          return Response({"message":serializer.errors})
        amount = request.data.get('amount')
        mobile_number = request.data.get('mobile_number')
        initiator_password = str(settings.INITIATOR_PASSWORD)
        certificate = str(settings.SANDBOX_CERTIFICATE)
        security = initiator_password+certificate
        message = security.encode('ascii')
        key = b"0123456789ABCDEF"  # 16-byte key for AES-128
        iv = b"1234567890123456" 
        openssl_encrypted_message = encrypt_data(message,key,iv)
        credential = settings.SAFARICOM_SECURITY_CREDENTIAL_B2C

        # serializer.save()

        # africastalking.initialize(settings.AFRICAS_TALKING_USERNAME,settings.AFRICAS_TALKING_API_KEY)
        # print({"afri_username":settings.AFRICAS_TALKING_USERNAME,"afri_key":settings.AFRICAS_TALKING_API_KEY})
        # sms = africastalking.SMS
        # recipient = ["+"+mobile_number]
        # sender = "M-MONEY"
        # message = "You have received kES"+amount

        payload = {    
            "OriginatorConversationID": str(''.join(random.choices(string.ascii_letters, k=64))),
            "InitiatorName": settings.INITIATOR_NAME,
            "SecurityCredential":settings.B2C_SECURITY_CREDENTIAL,
            "CommandID":settings.COMMANDID,
            "Amount":amount,
            "PartyA":"600980",
            "PartyB":mobile_number,
            "Remarks":"here are my remarks",
            "QueueTimeOutURL":settings.SAFARICOM_TIMEOUT_URL,
            "ResultURL":settings.SAFARICOM_RESULTURL,
            "Occassion":"Christmas"
        }
        try:
            res = requests.post(settings.SAFARICOM_B2C_ENDPOINT,headers=headers,json=payload)
            print(res.text)
            #if(res.status==200):    
            json_response = res.json()
            return Response({"safaricom":json_response})
        except Exception as e:
            return Response({"error":e})
        # message = 'You shall receive'+amount+'KES'
        # sender_id = "254sms"
        # phone = mobile_number
        # api_key = settings.SMS_KEY
        # username = settings.SMS_USERNAME
        # sms_url = 'https://api.254sms.com/version1/sendsms'
        # header = {
        # 'Content-Type': 'application/json',
        # }
        # data = {
        #     'username':username,
        #     'api_key':api_key,
        #     'sender_id':sender_id,
        #     'phone':phone,
        #     'message':message
        # }
        # sms_response = requests.post(sms_url,headers=header,json=data)
        # print(sms_response)
        # if sms_response.status_code==200:
        #     return Response({"sms_sending":sms_response})
        # else:
        #     return Response({"sms_sending":sms_response})
class ConvertToCrypto(APIView):
    serializer_class = MobileSerializer
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
          return Response({"message":serializer.errors})
        access_token = get_access_token()
        endpoint = settings.SAFARICOM_STK_PUSH
        Business_short_code = settings.BUSINESS_SHORT_CODE
        logger = logging.getLogger('django.server')
        logger.info(settings.SAFARICOM_STK_PUSH)
        logger.info(access_token)
        print("after logging")
        print(endpoint)

        timestamp = f"{datetime.datetime.now():%Y%m%d%H%M%S}"

        

        pass_key = settings.SAFARICOM_PASS_KEY

        message = str(Business_short_code)+str(pass_key)+str(timestamp)
        print("message",message)
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        password = base64_bytes.decode('ascii')

        print(password)

        print("pass key", pass_key)

        
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
        }
        amount = request.data.get('amount')
        mobile_number = request.data.get('mobile_number')

        print(headers)
        payload = {    
                    "BusinessShortCode": '174379',    
                    "Password": password,    
                    "Timestamp": timestamp,    
                    "TransactionType": "CustomerPayBillOnline",    
                    "Amount": amount,    
                    "PartyA":mobile_number,    
                    "PartyB":'174379',    
                    "PhoneNumber":mobile_number,    
                    "CallBackURL": settings.SAFARICOM_CALLBACK_URL,    
                    "AccountReference":"Test",    
                    "TransactionDesc":"Test"
                }
        print(endpoint)
        logging.info(endpoint)
        print("settings.SAFARICOM_CALLBACK_URL")
        response = requests.post(endpoint, json=payload, headers=headers)
        print(response.text)
        if response.status_code == 200:
            json_response = response.json()
           
            # Service.MerchantRequestID = json_response['MerchantRequestID']
            # Service.CheckoutRequestID = json_response['CheckoutRequestID']
            # Service.save()
            return Response({
                'status': True,
                'message': json_response
            }, status=status.HTTP_200_OK)
        else:
            json_response = response.json()
            print(endpoint)
            logging.info(endpoint)
            print(response.text)
            return Response({
                'status': False,
                'message': json_response
            }, status=status.HTTP_400_BAD_REQUEST)
        
class ToFiatTransactions(APIView):
    serializer_class = BusinessToCustomerSerializer
    def get(self, request):
        data = BusinessToCustomer.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)
    
class ToCryptoTransactions(APIView):
    serializer_class = StkPushSerializer
    def get(self, request):
        data = SuccesfulTransactions.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)

class CallBackUrl(APIView):
    def post(self, request):
        print('Call back started')
        print(request.data)
        data = request.data
        logger = logging.getLogger('django.server')
        logger.info(data['Body']['stkCallback'])
        resultCode = data['Body']['stkCallback']['ResultCode']
        logger.info(data)
        if resultCode == 0:
            succesfulTransactions = SuccesfulTransactions()
            succesfulTransactions.MerchantRequestID = data["Body"]["stkCallback"]["MerchantRequestID"]
            succesfulTransactions.CheckoutRequestID = data["Body"]["stkCallback" ]["CheckoutRequestID"]
            succesfulTransactions.ResultDesc = data["Body"]["stkCallback" ]["ResultDesc"]
            succesfulTransactions.Amount = data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0]["Value"]
            succesfulTransactions.MpesaReceiptNumber = data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"]
            succesfulTransactions.TransactionDate = data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][3]["Value"]
            succesfulTransactions.PhoneNumber = data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][4]["Value"]
            succesfulTransactions.save()
            return Response({"msg": "Successfully saved transaction"})
        else:
            cancelledTransactions = CancelledTransactions()
            cancelledTransactions.MerchantRequestID = data["Body"]["stkCallback"]["MerchantRequestID"]
            cancelledTransactions.CheckoutRequestID = data["Body"]["stkCallback" ]["CheckoutRequestID"]
            cancelledTransactions.ResultCode = data["Body"]["stkCallback"]["ResultCode"]
            cancelledTransactions.save()
            return Response({"msg": "Transaction was cancelled"})
           
        
class ResultUrl(APIView):
    def post(self, request):
        print("Result URL")
        print(request.data)
        data = request.data
        logger = logging.getLogger('django.server')
        logger.info(data["Result"])
        resultCode = data["Result"]["ResultCode"]
        logger.info(data)
        logger.info(resultCode)
        if resultCode == 0:
            businessToCustomer = BusinessToCustomer()
            businessToCustomer.ResultCode = resultCode
            businessToCustomer.ResultDesc = data["Result"]["ResultDesc"]
            businessToCustomer.ConversationID = data["Result"]["ConversationID"]
            businessToCustomer.Amount = data["Result"]["ResultParameters"]["ResultParameter"][0]["Value"]
            businessToCustomer.MpesaReceiptNumber = data["Result"]["ResultParameters"]["ResultParameter"][1]["Value"]
            businessToCustomer.PhoneNumber = data["Result"]["ResultParameters"]["ResultParameter"][2]["Value"]
            businessToCustomer.TransactionDate = data["Result"]["ResultParameters"]["ResultParameter"][3]["Value"]
            logger.info("Successful transaction")
            businessToCustomer.save()
            return Response({"reponse":"Successful transaction"})
        else:
            businessToCustomer = BusinessToCustomer()
            businessToCustomer.ResultCode = resultCode
            businessToCustomer.ResultDesc = data["Result"]["ResultDesc"]
            businessToCustomer.ConversationID = data["Result"]["ConversationID"]
            logger.info("Failed transaction")
            businessToCustomer.save()
            return Response({"reponse":"Failed transaction"})
        
      
    
class TimeOutUrl(APIView):
    def post(self, request):
        print(request.data)
        data = request.data
        json_response = json.dumps(data)
        logger = logging.getLogger('django.server')
        logger.info(data)
        return Response({"data":json_response})
class Donations(APIView):
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
          return Response({"message":serializer.errors})
        access_token = get_access_token()
        endpoint = settings.SAFARICOM_STK_PUSH
        Business_short_code = settings.BUSINESS_SHORT_CODE
        logger = logging.getLogger('django.server')
        logger.info(settings.SAFARICOM_STK_PUSH)
        logger.info(access_token)
        print("after logging")
        print(endpoint)

        timestamp = f"{datetime.datetime.now():%Y%m%d%H%M%S}"

        

        pass_key = settings.SAFARICOM_PASS_KEY

        message = str(Business_short_code)+str(pass_key)+str(timestamp)
        print("message",message)
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        password = base64_bytes.decode('ascii')

        print(password)

        print("pass key", pass_key)

        
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
        }
        amount = request.data.get('amount')
        mobile_number = request.data.get('mobile_number')

        print(headers)
        payload = {    
                    "BusinessShortCode": '174379',    
                    "Password": password,    
                    "Timestamp": timestamp,    
                    "TransactionType": "CustomerPayBillOnline",    
                    "Amount": amount,    
                    "PartyA":mobile_number,    
                    "PartyB":'174379',    
                    "PhoneNumber":mobile_number,    
                    "CallBackURL": settings.SAFARICOM_DONATIONS_CALLBACKURL,    
                    "AccountReference":"Test",    
                    "TransactionDesc":"Test"
                }
        print(endpoint)
        logging.info(endpoint)
        print("settings.SAFARICOM_CALLBACK_URL")
        response = requests.post(endpoint, json=payload, headers=headers)
        print(response.text)
        if response.status_code == 200:
            json_response = response.json()
           
            # Service.MerchantRequestID = json_response['MerchantRequestID']
            # Service.CheckoutRequestID = json_response['CheckoutRequestID']
            # Service.save()
            return Response({
                'status': True,
                'message': json_response
            }, status=status.HTTP_200_OK)
        else:
            json_response = response.json()
            print(endpoint)
            logging.info(endpoint)
            print(response.text)
            return Response({
                'status': False,
                'message': json_response
            }, status=status.HTTP_400_BAD_REQUEST)

class DonationsCallbackUrl(APIView):
    serializer_class = DonateSerializer
    def post(self, request):
        print('Call back started')
        print(request.data)
        data = request.data
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
          return Response({"message":serializer.errors})
        logger = logging.getLogger('django.server')
        logger.info(data['Body']['stkCallback'])
        resultCode = data['Body']['stkCallback']['ResultCode']
        logger.info(data)
        if resultCode == 0:
            donations = Donations()
            donations.ResultCode = resultCode
            donations.ResultDesc = data["Result"]["ResultDesc"]
            donations.ConversationID = data["Result"]["ConversationID"]
            donations.Amount = data["Result"]["ResultParameters"]["ResultParameter"][0]["Value"]
            donations.MpesaReceiptNumber = data["Result"]["ResultParameters"]["ResultParameter"][1]["Value"]
            donations.PhoneNumber = data["Result"]["ResultParameters"]["ResultParameter"][2]["Value"]
            donations.TransactionDate = data["Result"]["ResultParameters"]["ResultParameter"][3]["Value"]
            logger.info("Successful transaction")
            donations.save()
            return Response({"reponse":"Successful transaction"})
        else:
            donations = Donations()
            donations.ResultCode = resultCode
            donations.ResultDesc = data["Result"]["ResultDesc"]
            donations.ConversationID = data["Result"]["ConversationID"]
            logger.info("Failed transaction")
            donations.save()
            return Response({"reponse":"Failed transaction"})
