from rest_framework import serializers 
from map.models import PlacePost, PostLike, MapYourDiary
 
#  class ExtensionSerial
 
class MapYourDiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MapYourDiary
        fields = ('user_id', 'user_name')

class PlacePostSerializer(serializers.ModelSerializer):
    writer = MapYourDiarySerializer(read_only=True)
    likes = serializers.PrimaryKeyRelatedField(queryset=PostLike.objects.all(), many=True)

    class Meta:
        model = PlacePost
        fields = (
            'id',
            'title',
            'writer',
            'description',
            'likes',
            'lat',
            'lng'
        )

class LikeSerializer(serializers.ModelSerializer):
    liker = PlacePostSerializer(many=True, read_only=True)

    class Meta:
        model = PostLike
        fields = ('like_bool', 'liker')




