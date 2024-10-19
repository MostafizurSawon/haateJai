from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserAccount
from django import forms

class UserRegistrationForm(UserCreationForm):
    usable_password = None # register form correction
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
        
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit is True:

            # account = User(username = username, email=email, first_name = first_name, last_name = last_name)
            # print(account)
            # account.is_active = False
            # account.save()

            user.is_active = False
            user.save()
            
            # will create a new account when user registers
            # UserAccount.objects.create(
            #     user = user,
            # )
        return user
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        # fields = '__all__'
        fields = ['image','gender','hometown','mobile', 'age', 'address', 'description'] 
        
        labels = {
            'gender': 'Gender',
            'hometown': 'Hometown',
            'address': 'Address',
            'mobile': 'Mobile Number',
            'age': 'Age',
            'description': 'Short Description',
        }
        
class AddressForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['address'] 