from django import forms
from django.core.validators import validate_slug
from django.forms import widgets, TextInput, Textarea, ModelForm, SelectMultiple
from courses.models import Course

class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title','description','image','slug']
        labels = {
            'title': "Kurs Başlığı",
            'description':"Kurs Açıklaması",
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),
            

        }
        error_messages = {
            "title": {
                "required":"Kurs başlığı girilmesi zorunludur. ",
                "max_lenght": "Maksimum 50 karakter girebilirsiniz. ",
                
            },
            "description": {
                "required":"Kurs açıklaması girilmesi zorunludur. ",
                
            }
        }

class CourseEditForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title','description','image','slug','categories','isActive']
        labels = {
            'title': "Kurs Başlığı",
            'description':"Kurs Açıklaması",
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),
            "categories":SelectMultiple(attrs={"class":"form-control"})
            

        }
        error_messages = {
            "title": {
                "required":"Kurs başlığı girilmesi zorunludur. ",
                "max_lenght": "Maksimum 50 karakter girebilirsiniz. ",
                
            },
            "description": {
                "required":"Kurs açıklaması girilmesi zorunludur. ",
                
            }
        }


class uploadForm(forms.Form):
    image = forms.ImageField()





