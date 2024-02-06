# forms.py

from django import forms

class SubscriberForm(forms.Form):
    email = forms.EmailField(label='Enter your email', max_length=100)
