from allauth.account.forms import SignupForm
from django.shortcuts import redirect
from django.contrib import messages
import requests

class APISignupForm(SignupForm):
    def save(self, request):
        email = self.cleaned_data['email']
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        print(email, flush=True)
        print(password1, flush=True)
        print(password2, flush=True)

        url = "http://api:8001/api/auth/registration/"

        data = {
            'email': email,
            'password1': password1,
            'password2': password2,
        }

        response = requests.request("POST", url, data=data)

        print(response, flush=True)
        print(response.status_code, flush=True)

        if response.status_code==400:
            print("return redirect")
            return redirect('account_signup')
        else:
            user = super(APISignupForm, self).save(request)
            return user



    # def signup(self, request, user):
    #     email = self.cleaned_data['email']
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #
    #     print(email, flush=True)
    #     print(password1, flush=True)
    #     print(password2, flush=True)
    #
    #     url = "http://api:8001/api/auth/registration/"
    #
    #     data = {
    #         'email': email,
    #         'password1': password1,
    #         'password2': password2,
    #     }
    #
    #     response = requests.request("POST", url, data=data)
    #
    #     print(response, flush=True)
    #     print(response.status_code, flush=True)
    #     print(response.json(), flush=True)
    #     print(response.json()['email'], flush=True)
    #
    #     if response.status_code == 400:
    #         return redirect('front:home_view')
    #         print("return redirect")
    #     else:
    #         user.save()



    # def save(self, request):
    #     user = super(APISignupForm, self).save(request)
    #     user.email = self.cleaned_data['email']
    #     user.password1 = self.cleaned_data['password1']
    #     user.password2 = self.cleaned_data['password2']
    #     print(user.email, flush=True)
    #     print(user.password1, flush=True)
    #     print(user.password2, flush=True)
    #
    #     url = "http://api:8001/api/auth/registration/"
    #
    #     data = {
    #         'email': user.email,
    #         'password1': user.password1,
    #         'password2': user.password2,
    #     }
    #
    #     response = requests.request("POST", url, data=data)
    #
    #     print(response, flush=True)
    #     print(response.status_code, flush=True)
    #     print(response.json(), flush=True)
    #     print(response.json()['email'], flush=True)
    #
    #     if response.status_code == 400:
    #         return redirect('front:home_view')
    #         print("return redirect")
    #     else:
    #         user.save()
    #         return user
        #
        # if response.json()['email'][0] == 'A user is already registered with this e-mail address.':
        #     messages.error(request, "A user is already registered with this e-mail address 2.")
        #     return redirect('account_signup')
        # else:
        #     user.save()
        #     return user

    class Meta:
        # model = get_user_model()
        fields = ('email', 'password1', 'password2')
