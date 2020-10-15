from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm, RegisterForm


def home_view(request):
    return render(request, 'home.html', {})


def login_view(request):
    error_message = None
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        print(form.data)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')
            else:
                error_message = 'The username or password is not correct. Please try again.'

    return render(request, 'login.html', {'form': form, 'error_message': error_message})



def register_view(request):
    success_message = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print('POST request asked for')
        print(form.data)
        if form.is_valid():
            print('form.is_valid')
            form.save()
            print('form is_saved')
            username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username)
            # login(request, user)
            print('Your account has been created! You are now able to log in.')
            success_message = 'Your account has been created! You are now able to log in.'
            messages.success(request, 'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        print('GET request asked for')
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'success_message': success_message})