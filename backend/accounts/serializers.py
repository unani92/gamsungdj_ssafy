from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    from music.serializers import SongSerializer
    password = serializers.CharField(write_only=True)
    avatar = serializers.ImageField(source='userprofile.avatar')
    gender = serializers.CharField(source='userprofile.gender')
    age = serializers.CharField(source='userprofile.age')
    is_signed_up = serializers.BooleanField(source="userprofile.is_signed_up")
    like_songs = SongSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'avatar', 'gender', 'age', 'is_signed_up', 'like_songs')

    def create(self, validated_data, instance=None):
        avatar = validated_data.pop('avatar')
        gender = validated_data.pop('gender')
        age = validated_data.pop('age')
        profile_data = { 'avatar': avatar, 'gender': gender, 'age': age, 'is_signed_up': True }
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        UserProfile.objects.update_or_create(user=user, **profile_data)
        return user


