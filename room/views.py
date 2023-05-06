from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Room, Message

@login_required
def rooms(request):
    print(request.user)
    rooms = Room.objects.filter(members__username__in=[request.user.username])


    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
    members=room.members.all()

    return render(request, 'room/room.html', {'room': room, 'messages': messages,'members':members,'curuser':request.user})