from allauth.account.forms import SignupForm
import requests

class APISignupForm(SignupForm):
    def save(self, request):
        user = super(APISignupForm, self).save(request)
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        print(user.email, flush=True)
        print(user.password1, flush=True)
        print(user.password2, flush=True)

        url = "http://api:8001/api/auth/registration/"

        data = {
            'email': user.email,
            'password1': user.password1,
            'password2': user.password2,
        }

        response = requests.request("POST", url, data=data)

        print(response.json(), flush=True)

        user.save()
        return user

    class Meta:
        # model = get_user_model()
        fields = ('email', 'password1', 'password2')
