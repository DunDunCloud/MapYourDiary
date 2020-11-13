from rest_framework import serializers 
from map.models import User, Diary, Like
 
#  class ExtensionSerial
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_id',
            'user_name',
            'user_email'
        )

class DiarySerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only=True)

    class Meta:
        model = Diary
        fields = (
            'id',
            'writer',
            'title',
            'description',
            'lat',
            'lng'
        )

class LikeSerializer(serializers.ModelSerializer):
    liker = UserSerializer(read_only=True)
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Like
        fields = (
            'liker',
            'posts'
        )
