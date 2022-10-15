
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AppCoder.models import Avatar, Post

class ProfesionFormulario(forms.Form):   
    nombre= forms.CharField(max_length=200)


class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']

        help_texts = {k:"" for k in fields}

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email']


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }
