from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login

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
