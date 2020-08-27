from django import forms
from recipes_app.models import Author, Recipe

class RecipesAddForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    time_required = forms.CharField(max_length=15)

class ImageForm(forms.ModelForm):
    model = Recipe
    fields = [
        'name',
        'image'
    ]


class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=30)
    bio = forms.CharField(widget=forms.Textarea)