from django.contrib.auth.models import User
from users.models import Profile
from walkers.models import Walker
from rest_framework import generics, permissions
from rest_framework.response import Response

# Knox
from knox.models import AuthToken

from users.serializer import ProfileSerializer

from accounts.serializers import UserSerializer, RegisterSerializer, LoginSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    
        user = serializer.save()

        if request.data['role'] == 'Dueño':
            user_profile = Profile(user=user)
            user.role = 'Dueño'
            user_profile.save()
        
        elif request.data['role'] == 'Paseador':
            walker = Walker(user=user)
            user.role = 'Paseador'
            walker.save()

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        
        return Response({
            "user": UserSerializer(user, context= self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

#Get User
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


#Using Knox
# Login API
# class LoginAPI(KnoxLoginView):
#     permissions_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)