from django.contrib.auth.models import User
from django.db import models

class Interest(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    availCount =  models.IntegerField()

    def __str__(self):
        return self.name

class InterestUserRelation(models.Model):
    interest = models.ForeignKey(Interest, related_name='tags', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='tags', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


