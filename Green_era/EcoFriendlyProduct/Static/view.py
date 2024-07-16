from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
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