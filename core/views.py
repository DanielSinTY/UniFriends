from django.contrib.auth import login
from django.shortcuts import render, redirect
from room.rooms import CreateRoom
from .forms import SignUpForm
from .forms import interestForm,newInterestForm
from django.contrib.auth.models import User
from .models import InterestUserRelation,Interest
def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            # if user does not have rooms (i.e. new user), redirect to timetable.html
            # TO BE IMPLEMENTED
            if (True):
                return render(request, 'core/timetable.html')
            
            # else (i.e. not new user), go to rooms instead of frontpage
            # TO BE IMPLEMENTED
            

            # TO BE DELETED
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
                if i.availCount==6:
                    CreateRoom(i)
                    i.availCount=0
                i.save()


            return redirect('frontpage')
    else:
        form = interestForm()
    return render(request, 'core/interest.html', {'form': form})

def newinterest(request):
    if request.method == 'POST':
        form = newInterestForm(request.POST)

        if form.is_valid():
            newInterest=Interest(name=form.cleaned_data['newInterest'],availCount=0)
            newInterest.save()
            return redirect('interest')
    else:
        form = newInterestForm()
    return render(request, 'core/interest.html', {'form': form})

def timetable(request):
    return render(request, 'core/timetable.html')

def profile(request):
    return render(request, 'core/profile.html',{'interests':[i.interest for i in InterestUserRelation.objects.filter(user=request.user)]})