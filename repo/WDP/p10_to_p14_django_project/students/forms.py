from django import forms
from .models import Student


class StudentForm(forms.ModelForm):   # P13: ModelForm
    class Meta:
        model = Student
        fields = ["name", "email", "course", "marks"]
        widgets = {f: forms.TextInput(attrs={"class": "form-control"}) for f in ["name"]} | {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "course": forms.Select(attrs={"class": "form-select"}),
            "marks": forms.NumberInput(attrs={"class": "form-control"}),
        }
