from django.forms import ModelForm
from django import forms
from filmRating.models.Profile import Profile
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["user", "img"]

        widgets = {
            "user": forms.HiddenInput(),
            "img": forms.FileInput(attrs={"class": "form-control"}),
        }
