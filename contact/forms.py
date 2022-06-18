from django import forms

class Contactform(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    
    