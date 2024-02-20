from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import Profile

class EditProfileForm(forms.ModelForm):
    #user creation form auth.form olduğu için widgetler böyle oldu
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        #sıralaması görüntüyü belirler
        fields = ("username", "first_name", "last_name", "email")

class PasswordChangingForm(PasswordChangeForm):
    #user creation form auth.form olduğu için widgetler böyle oldu
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"class":"form-control", "type": "password", "placeholder": "Please Enter Your Current Password"}), label="Old Password")
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password", "placeholder": "Please Enter Your Mew Password"}), label="New Password")
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password", "placeholder": "Please Enter Your Mew Password Again"}), label="Confirm New Password")

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")

class ProfilePageForm(forms.ModelForm):
    bio = forms.CharField( max_length = 250, widget = forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'linkedin_url', 'facebook_url', 'twitter_url', 'instagram_url', 'youtube_url')

        widgets = {
                "website_url": forms.TextInput(attrs={"class": "form-control"}),
                "linkedin_url": forms.TextInput(attrs={"class": "form-control"}),
                "facebook_url": forms.TextInput(attrs={"class": "form-control"}),
                "twitter_url": forms.TextInput(attrs={"class": "form-control"}),
                "instagram_url": forms.TextInput(attrs={"class": "form-control"}),
                "youtube_url": forms.TextInput(attrs={"class": "form-control"}),
            }
