from django import forms

# Create your forms here.

class ContactForm(forms.Form):
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)
    email_address = forms.EmailField(max_length = 150)
