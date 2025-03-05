from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["mark", "text"]
        widgets = {
            "mark": forms.Select(attrs={"class": "form-select"}),
            "text": forms.Textarea(attrs={"class": "form-control", "placeholder": "Напишіть свій відгук...", "rows": 4}),
        }
