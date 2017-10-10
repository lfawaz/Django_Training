from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CreateUsers(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        self.fields['username'].labels = 'Display Name'
        self.fields['email'].labels = 'Email Address'
        self.fields['password1'].labels = 'Password'
        self.fields['password2'].labels = 'Confirm Password'
