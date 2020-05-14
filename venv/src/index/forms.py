from django import forms


class EmailForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Content'}))
