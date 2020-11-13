from rest_framework import serializers 
from map.models import MapPost
 
 
class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapPost
        fields = ('id',
                  'title',
                  'description',
                  'published'
                #   'lat',
                #   'lng'
                  )
