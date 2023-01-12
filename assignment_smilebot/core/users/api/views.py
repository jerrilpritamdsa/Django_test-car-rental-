from rest_framework import generics, status, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, RenterSerializer, OwnerSerializer
from rest_framework.views import APIView
from .permissions import IsOwnerUser, IsRenterUser


class RenterSignupView(generics.GenericAPIView):
    serializer_class = RenterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user":UserSerializer(user, context = self.get_serializer_context()).data,
            "token": Token.objects.get(user = user).key,
            "message":'Account created Successfully',
        })
        
class OwnerSignupView(generics.GenericAPIView):
    serializer_class = OwnerSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user":UserSerializer(user, context = self.get_serializer_context()).data,
            "token": Token.objects.get(user = user).key,
            "message":'Account created Successfully',
        })
        
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context = {'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'is_owner':user.is_owner,

        })
        

class LogoutView(APIView):
    def post(self, request):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)

class OwnerOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated&IsOwnerUser]
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user

class RenterOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated&IsRenterUser]
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user