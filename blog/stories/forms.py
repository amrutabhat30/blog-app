from django.forms import ModelForm
from django import forms
from stories.models import Story, Comment

# Create the form class.


class CreateStoryForm(ModelForm):
    """Form for creating a story"""
    title = forms.CharField(label="Title :", max_length=50,
                            error_messages={'required': 'Please enter a title for your story'})
    link = forms.URLField(label="Link :",max_length=100,
                          error_messages={'required': 'Please enter a link to your story'})
    # archive = forms.BooleanField(initial=False,required=False)

    class Meta:
        model = Story
        fields = ['title', 'link']


class CreateCommentForm(ModelForm):
    """Form for posting a comment"""
    text = forms.CharField(max_length=250, widget=forms.Textarea(attrs={'rows': 5, 'cols': 60}),
                           error_messages={'required': 'Please enter a comment for the story'})

    class Meta:
        model = Comment
        fields = ['text']
