# from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
from users.models import GrinchUser
# from picklist.models import Route


class GrinchUserCreationForm(UserCreationForm):
    # name = forms.CharField(max_length=100)
    # route = models.ForeignKey(Route, null=True, on_delete=models.PROTECT)
    # email = models.EmailField(max_length=128)

    class Meta:
        model = GrinchUser
        fields = '__all__'


class GrinchUserChangeForm(UserChangeForm):

    class Meta:
        model = GrinchUser
        fields = '__all__'
