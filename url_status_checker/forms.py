from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "username",
        "type": "text"
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "email",
        "type": "email"
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "password",
        "type": "password"
    }))
