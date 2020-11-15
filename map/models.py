from django.db import models, migrations
from djongo import models


class User(models.Model):
    user_id = models.CharField(max_length=50, blank=False, default='')
    user_name = models.CharField(max_length=50, blank=False, default='')
    user_email = models.EmailField()

    def __str__(self):
        return self.user_id


class Diary(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField()
    lat = models.FloatField(max_length=300, blank=False, default=0)
    lng = models.FloatField(max_length=300, blank=False, default=0)

    def __str__(self):
        return self.writer + self.id

class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Diary)
