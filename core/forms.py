from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Interest

class UserModelChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
         return obj.name
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class interestForm(forms.Form):


    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class newInterestForm(forms.Form):
    newInterest = forms.CharField(label='Your interest to be added', max_length=100)