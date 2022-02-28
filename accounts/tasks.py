from celery import shared_task
from kavenegar import *
from django.conf import settings


@shared_task
def send_otp_via_sms(auth_code, receiver):
    """
    A celery task to send Authentication code via SMS
    using kavenegar
    """
    api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
    params = {'receptor': receiver, 'token': auth_code, 'template': 'phone-verification'}
    api.verify_lookup(params)

