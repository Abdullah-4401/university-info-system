from django.urls import path
from .views import RegisterView, LoginView, LogoutView , get_csrf_token , ForgotPasswordView , ResetPasswordView 

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    
    path('csrf-token/',get_csrf_token,name='csrf-token'),
     path('forgot-password/',ForgotPasswordView.as_view(),name='forgot-password'),
    path('reset-password/<str:id>/<str:token>/',ResetPasswordView.as_view(),name='reset-password'),
]


