from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    with_password = forms.BooleanField(required=False)

class OTPLoginForm(forms.Form):
    otp_code = forms.CharField()