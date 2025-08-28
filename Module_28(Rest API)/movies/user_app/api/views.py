from watchlist_app import models
from .import serializers
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.save()
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


#logout view
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        return Response({'message':"Token deleted successfully."})
