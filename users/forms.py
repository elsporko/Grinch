from django impo9rt forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auto.models import User

class UserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    route = models.ForeignKey(Route, null=True, on_delete=models.PROTECT)
    email = models.EmailField(max_length=128)

    class Meta:
        model = User
        fields = ['username', 'name', 'route', 'email', 'password1', 'password2']

