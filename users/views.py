from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
         form = RegisterForm(request.POST)
         if  form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             email = form.cleaned_data.get('email')
             messages.success(request, f'Welcome {email} your account has been created')
             return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profilepage(request):
    return render(request,'users/profile.html')
