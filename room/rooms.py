from core.models import *
import random
import string
from django.utils.text import slugify
from .models import *

letters = string.ascii_lowercase


def CreateRoom(interest):
    users=InterestUserRelation.objects.filter(interest=interest)
    slug = slugify(interest.name)
    qs_exists = Room.objects.filter(slug=slug).exists()
    new_slug=slug
    while qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=''.join(random.choice(letters) for i in range(10))
        )
        qs_exists = Room.objects.filter(slug=new_slug).exists()
    newRoom=Room(name=interest.name,slug=new_slug,interest=interest)
    newRoom.save()
    for i in users:
        newRoom.members.add(i.user)
        i.delete()


