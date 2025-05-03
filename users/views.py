from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegisterUserSerializer

User = get_user_model()

class RegisterUser(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            user = User(email=email)
            user.set_password(password)
            user.save()
        return Response(True)
