from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(label="Full name",
                               max_length=100,
                               widget=forms.TextInput(
                                        attrs={'class': "form-control"}))
    email = forms.EmailField(label="Email address",
                             widget=forms.TextInput(
                                        attrs={'class': "form-control"}))
    phone = forms.CharField(required=False,
                            label="Phone number",
                            widget=forms.TextInput(
                                        attrs={'class': "form-control"}))
    message = forms.CharField(label="Message",
                              widget=forms.TextInput(
                                        attrs={'class': "form-control"}))
