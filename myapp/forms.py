from django import forms

class CreateNewTask (forms.Form):
    title = forms.CharField(label="Titulo", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class CreateNewProject (forms.Form):
    title = forms.CharField(label="Titulo", max_length=200)