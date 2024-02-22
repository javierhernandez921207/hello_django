from django import forms

class CreateNewTask (forms.Form):
    title = forms.CharField(label="Titulo", max_length=200)
    description = forms.CharField(widget=forms.Textarea)

class CreateNewProject (forms.Form):
    title = forms.CharField(label="Titulo", max_length=200)