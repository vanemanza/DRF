from rest_framework import serializers
from .models import Video
from  django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class VideoSerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'user']

