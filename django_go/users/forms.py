from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django.core.exceptions import ValidationError

access_key_list =['TEST1', 'TEST2', 'TEST3']
sex_choices = (
    ('MEN', 'men'),
    ('WOMEN', 'women')
)

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget= forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль', widget= forms.TextInput(attrs={'class':'form-control'}))




class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget= forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(label= 'Пол пользователя', choices=sex_choices,
                               help_text='MEN or WOMEN',widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label='возраст', widget=forms.TextInput(attrs={'class': 'form-control'}))
    access_key = forms.CharField(label='Ключ доступа', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email','gender' ,'age','access_key')


    def clean_access_key(self):
        access_key = self.cleaned_data['access_key']
        if access_key not in access_key_list:
            raise ValidationError('Неверный ключ регистрации')
        return access_key





class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender', 'age')