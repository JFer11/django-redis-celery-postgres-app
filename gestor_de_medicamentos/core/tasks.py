import datetime

from celery import shared_task
from core.models import User
from core.serializers import MedicamentoSerializer
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404


@shared_task
def send_an_email(subject, body, email_from, email_to):
    """
    @param: email_to must be a list of strings, for example: ["no-reply@moonlads.com"]
    """
    email = EmailMessage(
        subject,  # Subject
        body,  # Body
        email_from,  # Email From
        email_to,  # Email To
    )
    try:
        email.send()
        return True
    except:
        print("------------------------------")
        print("No email was sent.")
        print("------------------------------")
        return False
