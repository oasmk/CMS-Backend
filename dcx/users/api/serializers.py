from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import serializers
from users.models import AdminProfile


class AdminRegistrationSerializer(RegisterSerializer):

    def custom_signup(self, request, user):
        AdminProfile.objects.create(user=user)
        user.save()
