from django.forms import ModelForm,TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import City
from django import forms

class CityForm(ModelForm):
    class Meta:
        model = City
        fields=['name']
        widgets= {'name': TextInput(attrs={'class' : 'input','placeholder': 'City Name'})}

# class login(ModelForm):
#     class Meta:
class NewUserForm (UserCreationForm):
    class Meta:
        model = User
        email = forms.EmailField(required=True)
        fields = ("username","email","password1","password2")

    def save(self, commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user