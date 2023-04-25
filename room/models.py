from django.contrib.auth.models import User
from django.db import models
from core.models import Interest


class Room(models.Model):
    name = models.CharField(max_length=255)
    interest = models.ForeignKey(Interest, related_name='roomInterest', on_delete=models.PROTECT,blank=True,null=True)
    slug = models.SlugField(unique=True)
    members=models.ManyToManyField(User,blank=True,null=True,related_name='members')

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)