from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from forms import UserRegistrationForm



from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form.add_error(None, 'Error in Registration')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main')  # Redirect to your home page
                else:
                    form.add_error(None, 'This account is inactive.')
            else:
                form.add_error(None, 'Invalid username or password.')  # General error for security
        # If the form is not valid, the form will automatically display the default error messages
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form': form})