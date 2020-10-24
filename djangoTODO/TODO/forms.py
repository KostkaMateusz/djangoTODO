from django import forms

class AddTASK(forms.Form):
    title = forms.CharField(label='taks title', max_length=100)
    contex = forms.CharField(label='task contex', max_length=255)