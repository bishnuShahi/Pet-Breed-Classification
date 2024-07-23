from django import forms
from django.contrib.auth.models import User 

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length = 100, 
        required = True, 
        widget = forms.TextInput(
            attrs={
            'class':'my-[0.5rem] mx-0 w-full border-[1px] border-red-900 rounded h-[7%] px-[5px] py-[2px]',
            'placeholder':'john123'})
        )
    
    password = forms.CharField(
        required = True,
        widget = forms.PasswordInput(
            attrs={
                'class': 'my-[0.5rem] mx-0 w-full border-[1px] border-red-900 rounded h-[7%] px-[5px] py-[2px]',
                'placeholder': 'At least 8 characters'
            }
        )
    )
    
class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'my-[0.5rem] mx-0 w-full border-[1px] border-red-900 rounded h-[7%] px-[5px] py-[2px] mt-[1rem] ease-linear duration-200',
                'placeholder': 'john123'
                }
            ),
        label='Username'
        )
    
    name = forms.CharField(
        max_length=100, 
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'my-[0.5rem] mx-0 w-full border-[1px] border-red-900 rounded h-[7%] px-[5px] py-[2px] mt-[1rem] ease-linear duration-200',
                'placeholder': 'John Doe'
                }
            ),
         label='Full Name'
        )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'my-[0.5rem] mx-0 w-full border-[1px] border-red-900 rounded h-[7%] px-[5px] py-[2px] mt-[1rem] ease-linear duration-200',
                'placeholder': 'At least 8 characters'
            }
        ),
        label='Password'
    )
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'my-[0.5rem] mx-0 w-full border-[1px] border-red-900 rounded h-[7%] px-[5px] py-[2px] ease-linear duration-200',
            'placeholder': 'Same as password'
        }),
        label='Confirm Password'
    )
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and (confirm_password != password):
            self.add_error(None, 'Passwords do not match!')