from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets
from django.contrib import messages
from django import forms


class loginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if username == "admin":
            messages.add_message(self.request, messages.SUCCESS, f"Hoşgeldin {username}!")
            
        return username

    def confirm_login_allowed(self, user):
        if user.username.startswith("l"):
            raise forms.ValidationError("Bu kullanıcı adı ile giriş yapamazsınız. ")


