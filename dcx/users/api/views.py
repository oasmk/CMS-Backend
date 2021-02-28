from rest_auth.registration.views import RegisterView
from .serializers import AdminRegistrationSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from users.models import AdminProfile, CustomUser
from rest_framework import status, generics


class AdminRegistrationView(RegisterView):
    serializer_class = AdminRegistrationSerializer
