from django import forms 

class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, label='Task', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))