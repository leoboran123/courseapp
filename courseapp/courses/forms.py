from django import forms
from django.core.validators import validate_slug

class CourseCreateForm(forms.Form):
    title = forms.CharField(
        label="Kurs Başlığı", 
        error_messages={
        "required":"Kurs başlığı alanı zorunludur! "
        }, 
        widget=forms.TextInput(attrs={"class":"form-control"})
        )
    description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    slug = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),validators=[validate_slug])
    

