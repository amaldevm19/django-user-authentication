from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from .models import User


def home(request):
    return render(request, 'users/base.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.set_password(form.cleaned_data.get('password'))
            save_form.save()
            messages.success(request, 'User registered successfully')
            return redirect('signup')
        else:
            return render(request, 'users/signup.html', {'form': form})
    return render(request, 'users/signup.html')

def login(request):
    if request.method == 'POST':
        pass
    return render(request, 'users/login.html')

def reset_password(request):
    pass

def activate_mail(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
        if user is not None:
            user.is_verified = True
            user.save()
            messages.success(request, "Email confirmation done successfully")
            return redirect('login')
    except User.DoesNotExist:
        messages.error(request, "Please signup")
        return redirect('signup')

