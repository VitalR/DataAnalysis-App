from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=220)
    password = forms.CharField(max_length=220, widget=forms.PasswordInput)

    def clean(self):
        data = self.cleaned_data

        username = data.get('username')
        password = data.get('password')

        # logic for custom validation
        # if len(username) < 3:
        #     raise ValidationError('The Username is too short')
        # return username

        # if len(password) < 3:
        #     raise ValidationError('The password is too short')
        # return password

        return data