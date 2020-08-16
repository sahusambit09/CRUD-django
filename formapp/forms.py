from django import forms
from .models import User


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
class UserForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    mobile = forms.CharField()
    image = forms.FileField()
    document = forms.FileField()
