from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Product,OrderItem

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_nursery_manager')
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['manager_id']

        
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_nursery_manager')