from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.utils.encoding import force_bytes ,  force_str
from .serializers import UserSerializer, ForgotPasswordSerializer, LoginSerializer , ResetPasswordSerializer
from django.core.mail import send_mail
from django.conf import settings


@api_view(['GET'])
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken':request.COOKIES.get('csrftoken')})

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                return Response({'message': f'{user.username} is registered successfully'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer =LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return Response({'message':f'{user.username} is logged in successfully'},status=status.HTTP_200_OK)

            else:
                return Response({'error':'Invalid Input,Try Again'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user 
        logout(request)
         
        return Response({'message':f'{user.username} is logged out successfully'},status=status.HTTP_200_OK)


class ForgotPasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer=ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user=User.objects.get(email=email)
                token=default_token_generator.make_token(user)
                id=urlsafe_base64_encode(force_bytes(user.pk))
                resetlink=f'http://127.0.0.1:8000/auth/reset-password/{id}/{token}/'
                
                send_mail(
                    'Password Reset Request',
                    f'Please use the following link to reset your password:{resetlink}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                
                return Response({'message':'Password reset email sent'},status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error':'User with this email does not exist'},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request,*args,**kwargs):
        id=kwargs.get('id')
        token=kwargs.get('token')

        try:
            uid=force_str(urlsafe_base64_decode(id))
            user=User.objects.get(pk=uid)
        except (User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user,token):
            serializer =ResetPasswordSerializer(data=request.data)
            if serializer.is_valid():
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response({'message':'Password has been reset'}, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'Invalid User'}, status=status.HTTP_400_BAD_REQUEST)