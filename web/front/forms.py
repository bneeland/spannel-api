from django import forms
from allauth.account.forms import SignupForm

class APISignupForm(SignupForm):
    class Meta:
        # model = get_user_model()
        fields = ('email', 'password1', 'password2')
