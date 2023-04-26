from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from google.auth import jwt
from .models import User
import constants
from rest_framework.authtoken.models import Token
from .serializer import User_serializer
from social_user_info.social_user_info import APIService

# Create your views here.

@api_view(['POST'])
def register_with_google(request):
    data = request.data
    user_data = APIService.get_user_info(data['access_token'] , "google")
    
    if data['user_type'] not in [constants.user_types.client , constants.user_types.transporter]:
        return Response({"error":["user_type"] } , status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User(
            name = user_data['name'],
            email = user_data['email'],
            password = User.encode_password(user_data['id']),
            user_type = data['user_type'],
            google_login = True,
            verified = user_data['verified_email']
        )
        
        
        user.save()
        user.refresh_from_db()
    except:
        return Response({
            'error':['email'],
            'msg':"Email already exists"
            })
    
    serialized = User_serializer(user)
    
    return Response({
        'data' : {'user_data' : serialized.data},
        'msg':f"{user.name} Sucessfully added"
        },status=status.HTTP_200_OK)
    
    
    
@api_view(['POST'])
def sigin_with_google( request):
    data = request.data
    user_data = APIService.get_user_info(data['access_token'] , "google")
    print(user_data)
    if data['user_type'] not in [constants.user_types.client , constants.user_types.transporter]:
        return Response({"error":{"user_type"} } , status=status.HTTP_400_BAD_REQUEST)
    
    try:
    # find user in database
        user = User.objects.get(email = user_data['email'])
        if (User.decode_password(user.password) == user_data['id'] ) and user.google_login and user.verified:
            print( User.decode_password(user.password)  ,user.verified, user.google_login)
            token,_ = Token.objects.get_or_create(user = user)
            serialized = User_serializer(user)
            return Response({'data':{
                'token' : token.key,
                'user_data' :serialized.data,
                'msg':"Success fully Signed In"
            }})
        else :
            return Response({'error':['password'] , 
                                'msg':"Unable to match Id"} , status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'error':['user'] , 
                             'msg':"Unable to find user"} , status=status.HTTP_400_BAD_REQUEST)
        
    
    