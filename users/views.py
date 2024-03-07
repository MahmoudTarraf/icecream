from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import  get_object_or_404


from django.contrib.auth.models import User

from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get("username")
        password = request.data.get("password")
        if username and password:
            try:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
                token, created = Token.objects.get_or_create(user=user)
                serializer = UserSerializer(instance=user)
                return Response({"token": token.key, "user": serializer.data})
            except User.DoesNotExist:
                return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail": "Invalid request data."}, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data["username"])
            user.set_password(request.data["password"])
            user.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key, "user": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.email))
