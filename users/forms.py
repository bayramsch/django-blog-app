from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import Profile

class UserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', )
        
    def clean_email(self):
        email = self.cleaned_data['email'] # veya request.POST.get("email") olabilir
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Please use another email, that one already taken")
        
        return email
            
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("image", "bio",)
        

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")
        
class PasswordResetEmailCheck(PasswordResetForm):
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("There is no email")
        return email