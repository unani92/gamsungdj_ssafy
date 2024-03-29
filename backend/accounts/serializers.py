from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile, UserPlayList

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='userprofile.nickname')
    password = serializers.CharField(write_only=True)
    avatar = serializers.ImageField(source='userprofile.avatar', use_url=True, required=False)
    gender = serializers.CharField(source='userprofile.gender')
    age = serializers.CharField(source='userprofile.age')
    is_signed_up = serializers.BooleanField(source="userprofile.is_signed_up")

    class Meta:
        model = User
        fields = ('id', 'email', 'nickname', 'username', 'password', 'avatar', 'gender', 'age', 'is_signed_up', 'like_songs', 'like_albums')

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


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer
    avatar = serializers.ImageField(required=False, use_url=True)
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserPlayListSerializer(serializers.ModelSerializer):
    from music.serializers import SongSerializer
    user = UserSerializer(required=False)
    song = SongSerializer(read_only=True, many=True)

    class Meta:
        model = UserPlayList
        fields = '__all__'
