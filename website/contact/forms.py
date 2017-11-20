"""
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    subject = models.CharField(max_length=70)
    message = models.CharField(max_length=500)

"""

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50,label="Nome")
    email = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=30)
    subject = forms.CharField(max_length=70)
    message = forms.CharField(max_length=500)
