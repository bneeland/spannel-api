from allauth.account.forms import SignupForm
from django.shortcuts import redirect
from django.contrib import messages
import requests

from . import models

class APISignupForm(SignupForm):
    def save(self, request):
        email = self.cleaned_data['email']
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        url = "http://api:8001/api/auth/registration/"

        data = {
            'email': email,
            'password1': password1,
            'password2': password2,
        }

        response = requests.request("POST", url, data=data)

        if response.status_code==400:
            return redirect('account_signup')
        else:
            user = super(APISignupForm, self).save(request)
            models.Key.objects.create(token=response.json()['key'], user=user)
            return user
