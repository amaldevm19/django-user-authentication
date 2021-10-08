from django import forms
from .models import User
from django.core.exceptions import ValidationError

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'phone_number']

    def clean_username(self):
        username = self.cleaned_data['username']
        if username in [entry.username for entry in User.objects.all()]:
            raise ValidationError('User already exist')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email in [entry.email for entry in User.objects.all()]:
            raise ValidationError("Email not available for use")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password can't be less than 8 characters")
        if password.isalpha() or password.isnumeric():
            raise ValidationError("Password should contains both letters and numbers")
        return password

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number == '':
            pass
        else:
            if phone_number in [entry.phone_number for entry in User.objects.all()]:
                raise ValidationError("phone number not available for use")
            return phone_number



