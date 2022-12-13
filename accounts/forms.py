from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from . models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email']


class HealthFormCreation(ModelForm):
    class Meta:
        model = HealthForm
        fields = '__all__'