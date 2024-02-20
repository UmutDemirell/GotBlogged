from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list("name","name")

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "category", "snippet", "body", "header_image")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder":"Please Enter Your Blog Title"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control", "placeholder":"Please Enter Your Blog Title Tag"}),
            "category": forms.Select(choices = choice_list, attrs={"class": "form-control"}),
            "snippet": forms.Textarea(attrs={"class": "form-control", "placeholder":"Please Enter Your Blog Snippet"}),
            "body": forms.Textarea(attrs={"class": "form-control", "placeholder":"Please Enter Your Blog Context"}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "snippet", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder":"Please Enter Your Blog Title"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control", "placeholder":"Please Enter Your Blog Title Tag"}),
            "snippet": forms.Textarea(attrs={"class": "form-control", "placeholder":"Please Enter Your Blog Snippet"}),
            "body": forms.Textarea(attrs={"class": "form-control", "placeholder":"Please Enter Your Blog Context"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)

        widgets = {
            "body": forms.Textarea(attrs={"class": "form-control", }),
        }