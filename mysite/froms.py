from django import forms


class ModelForm(forms.Form):
    context = forms.CharField(max_length=300, widget=forms.Textarea)