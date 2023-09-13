from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'phone', 'avatar', 'country']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
