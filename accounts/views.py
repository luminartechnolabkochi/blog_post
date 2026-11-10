from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from accounts.serializers import UserSerializer

class UserCreateView(CreateAPIView):

    serializer_class = UserSerializer