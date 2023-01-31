from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from posts.models import Posts, Profile


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ['image', 'name']
        widgets = {
            'name': forms.Textarea(attrs={'cols': 60, 'rows': 17}),
        }

class AddProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'gender']
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 60, 'rows': 17}),
        }

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput)
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'gender']

