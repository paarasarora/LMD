from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError

# Create your views here.
class register(APIView):
    def post(self,request):
        username = request.data['username']
        if User.objects.filter(username = username).last():
            raise ValidationError({'message':['already exists']})
        if request.POST.get('user_type') is None:
            raise ValidationError({'message':['user_type cannot be null']})
        user_type = request.POST.get('user_type')
        user = User(username = username,user_type = user_type)
        password = request.data['password']
        user.set_password(password)
        refresh = RefreshToken.for_user(user)
        user.save()
        # name = User.objects.filter(username = username).last()

        return Response({'message': 'success my nigga',
        'user_id': user.id,
        'user_type':user.user_type,
        'refresh': str(refresh),
        'access': str(refresh.access_token)})