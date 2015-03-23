from django import forms
from MyStreet.models import Comment, Street, UserProfile
from django.contrib.auth.models import User


class StreetForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the street name.")
    location = forms.CharField(max_length=128, help_text="Please enter the street Location.")

    class Meta:
        model = Street
        fields = ('name','location','image')


class CommentForm(forms.ModelForm):
    safety_rate = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'rating', 'min':0, 'max':5,'step':1}), help_text="Safety:")
    business_rate = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'rating', 'min':0, 'max':5,'step':1}),help_text="Business:")
    infrastructure_rate = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'rating', 'min':0, 'max':5,'step':1}),help_text="Infrastructure:")
    comment = forms.CharField(max_length=128, widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ('safety_rate', 'business_rate', 'infrastructure_rate', 'comment')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)