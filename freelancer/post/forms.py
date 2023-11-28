from django import forms
from .models import Post


class PostForm2(forms.Form):
    title = forms.CharField(label="Title",
                            max_length=200,
                            widget=forms.TextInput(
                               attrs={'class': "form-control"}))
    body = forms.CharField(label="Body",
                           widget=forms.Textarea(
                               attrs={'class': "form-control"}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
        # fields = '__all__'
        # exclude = ["created"]
        widgets = {
                    "title": forms.TextInput(attrs={'class': "form-control"}),
                    "body": forms.Textarea(attrs={'class': "form-control", "cols": 80, "rows": 10}),
        }
        labels = {
            "title": "Title",
            "body": "Body",
        }
        help_texts = {
            "title": "Some useful help text.",
        }
        error_messages = {
            "title": {
                "max_length": "This title is too long.",
            },
        }

