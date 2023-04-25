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
    # def __init__(self, *args, **kwargs):
    #     super(interestForm, self).__init__(*args, **kwargs)
    #     self.fields['interest'] = forms.ModelChoiceField(
    #         queryset=Interest.objects.all()
    #     )
    #
    # class Meta:
    #     model = Interest
    # choices=zip(Interest.objects.values_list('name'),Interest.objects.values_list('slug'))

    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )