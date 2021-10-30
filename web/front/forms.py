from django import forms
from allauth.account.forms import SignupForm

class APISignupForm(SignupForm):
    def save(self, request):
        user = super(APISignupForm, self).save(request)
        user.email = self.cleaned_data['email']
        print(user.email, flush=True)
        user.save()
        return user

    class Meta:
        # model = get_user_model()
        fields = ('email', 'password1', 'password2')
