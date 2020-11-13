from django.db import models, migrations
from djongo import models


class MapYourDiary(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50, blank=False)
    user_name = models.CharField(max_length=50, blank=False, default='')


class PostLike(models.Model):
    like_bool = models.BooleanField(default=False)


class PlacePost(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    writer = models.ForeignKey(MapYourDiary, on_delete=models.CASCADE)
    description = models.TextField()
    likes = models.ManyToManyField(PostLike, related_name="liker", blank=False, default=0)
    # 위도
    lat = models.FloatField(max_length=300, blank=False, default=0)
    # 경도
    lng = models.FloatField(max_length=300, blank=False, default=0)

    

# class MapPost(models.Model):
#     title = models.CharField(max_length=70, blank=False, default='')
#     description = models.CharField(max_length=200,blank=False, default='')
#     published = models.BooleanField(default=False)
#     lng = models.FloatField(max_length=400, blank=False, default=0)
#     lat = models.FloatField(max_length=400, blank=False, default=0)
    
