from users.models import Profile
from walkers.models import Walker
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField('_get_user_role_')
    id = serializers.SerializerMethodField('_get_role_id_')

    def _get_role_id_(self, driver_object):
        id = getattr(driver_object, 'id')

        try:
            walker = Walker.objects.get(user_id = id)

            if walker.user_id == id:
                return walker.id
            
        except:
            pass

        try:
            owner = Profile.objects.get(user_id = id )
            if owner.user_id == id:
                return owner.id
        except :
            pass

    def _get_user_role_(self, driver_object):
        id = getattr(driver_object, 'id')

        try:
            walker = Walker.objects.get(user_id = id)

            if walker.user_id == id:
                return 'Paseador'
            
        except:
            pass

        try:
            owner = Profile.objects.get(user_id = id )
            if owner.user_id == id:
                return 'Dueño'
        except :
            pass

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role' )

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)

        if user and user.is_active:
            return user
        raise serializers.ValidationError("Usuario o contraseña incorrectos")