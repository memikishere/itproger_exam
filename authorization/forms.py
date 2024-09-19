from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Link


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    # меняю параметры полей
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['email'].required = True
        self.fields['email'].unique = True
        self.fields['username'].help_text = None

        
    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     email = self.cleaned_data['email']
    #     user.username = email[:email.index('@')]
    #     if commit:
    #         user.save()
    #     return user


class UserSettingsForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(label='Имя пользователя')

    class Meta:
        model = User
        fields = ['username', 'email']

class NewLinkForm(forms.ModelForm):
    link = forms.CharField(label='Ссылка')
    link_name = forms.CharField(label='Имя для ссылки')

    class Meta:
        model = Link
        fields = ['link', 'link_name']
    
    # def save(self, commit=True, value=None):
    #     user = super(NewLinkForm, self).save(commit=False)
    #     print(value)
    #     user.user = value
    #     if commit:
    #         user.save()
    #     return user