# Django
from rest_framework import serializers

# Models
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'photo', 'user_id', 'is_owner')
        depth = 1