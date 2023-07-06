from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_frameworksimplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
@api_view(["POST"])
def change_email(request):
    if request.method == "POST":
        user_id = request.data.get("user_id")
        email= request.data.get("email")
        if User.objects.filter(email=email).exists():
                return Response({'status': "User already exists"}, status=status.HTTP_409_CONFLICT)
        user = get_object_or_404(User, pk=user_id)
        user.email = email
        user.save()
        return Response({"status": "changed"})

@api_view(['POST'])
def change_password(request):
    if request.method == "POST":
        user_id = request.data.get("user_id")
        user = get_object_or_404(User, pk=user_id)
        password = request.data.get("password")
        user.password = make_password(password)
        user.save()
        return Response({"status": "changed"})

@api_view(['POST'])
def reset_password(request):
    if request.method == "POST":
        user_email = request.data.get("email")
        user = get_object_or_404(User, email=user_email)
        password = request.data.get("password")
        user.password = make_password(password)
        user.save()
        return Response({"status": "changed"})

@api_view(["POST"])
def change_username(request):
    if request.method == "POST":
        user_id = request.data.get("user_id")
        user_name= request.data.get("username")
        if User.objects.filter(username=user_name).exists():
                return Response({'status': "User already exists"}, status=status.HTTP_409_CONFLICT)
        user = get_object_or_404(User, pk=user_id)
        user.username = user_name
        user.save()
        return Response({"status": "changed"})
class MyTokenObtainPair(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # serializer = UserSerializerWithToken(self.user).data
        # for k,v in serializer.items():
        # data[k] = v
        user_profile = Profile.objects.get(user = self.user)
        data['profile_id'] = user_profile.id
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        return data
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPair


@api_view(["POST"])
def signup(request):
    if request.method == "POST":
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        if User.objects.filter(email=email).exists():
            return Response({'status': "User already exists"}, status=status.HTTP_409_CONFLICT)
        user = User.objects.create_user(username=username, email=email, password=make_password(password))
        user.save()
        profile = Profile.objects.create(user=user)
        profile.save()
        return Response({"status": "created"})
