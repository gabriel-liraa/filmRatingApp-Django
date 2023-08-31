from django import forms
from django.forms import ModelForm
from filmRating.models.Rating import Rating


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ["user", "film_rated", "value", "description"]
        labels = {
            "value": "Nota",
            "description": "Descrição",
        }
        widgets = {
            "user": forms.HiddenInput(),
            "film_rated": forms.HiddenInput(),
            "value": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                }
            ),
        }
