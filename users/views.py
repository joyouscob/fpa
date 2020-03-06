from django.shortcuts import render, redirect
from django.contrib import messages
#extended registration module
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        #instantiate if POST
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #clean data for use in flash message
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            #redirect to the admin page
            return redirect('fpa-admin')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
