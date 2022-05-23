from core.models import User
from core.serializers import UserSerializer
from core.tasks import send_an_email
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


@api_view(['GET'])
def home(request):
    send_an_email.delay('Subject', 'Hola', 'dgibert1@gmail.com', ['jpalgort@gmail.com'])
    return Response("HOLA")
