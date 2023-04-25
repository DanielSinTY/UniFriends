from django.contrib.auth import login
from django.shortcuts import render, redirect
from room.rooms import CreateRoom
from .forms import SignUpForm
from .forms import interestForm
from django.contrib.auth.models import User
from .models import InterestUserRelation
def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})

def setinterest(request):
    if request.method == 'POST':
        form = interestForm(request.POST)

        if form.is_valid():
            newInterests=form.cleaned_data['interests']
            for i in InterestUserRelation.objects.filter(user=request.user):
                i.interest.availCount-=1
                if i.interest.availCount<0:
                    i.interest.availCount=0
                i.interest.save()
                i.delete()
            for i in newInterests:
                i.availCount+=1
                newInterest = InterestUserRelation(interest=i, user=request.user)
                newInterest.save()
                if i.availCount==10:
                    CreateRoom(i)
                    i.availCount=0
                i.save()


            return redirect('frontpage')
    else:
        form = interestForm()
    return render(request, 'core/interest.html', {'form': form})
