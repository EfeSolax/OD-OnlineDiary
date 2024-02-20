from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class RegisterForm(forms.Form):
    attrs_username = {
        "placeholder": "Kullanıcı adı",
        "style":"""
width: 350px; 
height: 45px; 
border-radius: 10px;
margin-bottom: 15px;
font-size: 22px;
    """
    }

    attrs_email = {
        "placeholder": "Email",
        "style":"""
width: 350px; 
height: 45px; 
border-radius: 10px;
margin-bottom: 15px;
font-size: 22px;
    """
    }

    attrs_password = {
        "placeholder": "Parola",
        "style":"""
width: 350px; 
height: 45px; 
border-radius: 10px;
margin-bottom: 15px;
font-size: 22px;
    """
    }

    attrs_confirmation = {
        "placeholder": "Parola Doğrula",
        "style":"""
width: 350px; 
height: 45px; 
border-radius: 10px;
margin-bottom: 15px;
font-size: 22px;
    """
    }

    attrs_name = {
        "placeholder": "İsim soyisim",
        "style":"""
width: 350px; 
height: 45px; 
border-radius: 10px;
margin-bottom: 15px;
font-size: 22px;
    """
    }

    name = forms.CharField(label = "İsim soyisim", widget = forms.TextInput(attrs = attrs_name))
    username = forms.CharField(max_length=100, label = "Kullanıcı Adı", widget = forms.TextInput(attrs = attrs_username))
    email = forms.EmailField(label = "Email", widget = forms.EmailInput(attrs = attrs_email))
    password = forms.CharField(label = "Parola", widget = forms.PasswordInput(attrs = attrs_password))
    confirmation = forms.CharField(label = "Parola Doğrula", widget = forms.PasswordInput(attrs = attrs_confirmation))
    

    def clean(self):
        name = self.cleaned_data.get("name")
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirmation = self.cleaned_data.get("confirmation")

        if (username and email and password and confirmation and name) and password != confirmation:
            raise forms.ValidationError("Lütfen tüm alanları doldurunuz. Ve parolaların eşleştiğinden emin olunuz.")
        
        values = {
            "username": username,
            "email": email,
            "password": password,
            "confirmation": confirmation,
            "name": name,
        }

        return values
    
class LoginForm(forms.Form):
    attrs_username = {
        "placeholder": "Kullanıcı adı",
        "style":"""
width: 350px; 
height: 45px; 
border-radius: 10px;
margin-bottom: 25px;
font-size: 22px;
    """
    }
    
    attrs_password = {
        "placeholder": "Parola",
        "style":"""
width: 350px; 
height: 45px; 
border-radius: 10px;
margin-bottom: 25px;
font-size: 22px;
    """
    }
    
    attrs_email = {
        "placeholder": "Email",
        "style":"""
width: 350px; 
height: 45px; 
border-radius: 10px;
margin-bottom: 25px;
font-size: 22px;
    """
    }

    username = forms.CharField(max_length=100, label="Kullanıcı Adı", widget = forms.TextInput(attrs= attrs_username))
    password = forms.CharField(label = "Parola", widget = forms.PasswordInput(attrs = attrs_password))
    email = forms.EmailField(label = "Email", widget = forms.EmailInput(attrs = attrs_email))
    
