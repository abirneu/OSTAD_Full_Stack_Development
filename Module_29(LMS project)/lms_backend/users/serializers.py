from rest_framework import serializers
from . import User
from django.contrib.auth.hashers import make_password

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True)

    class meta:
        model = User
        fields = ['id', 'username', 'email','role','mobile_no','password']
        def create(self, validated_data):
            validated_data['password'] = make_password(validated_data['password'])
            return super().create(validated_data)