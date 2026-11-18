from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



def registro_view(request):
    if request.user.is_authenticated:
        return redirect('core:home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:home')

    else:
        form = UserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/registro.html', context=context)



def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:home')

    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('core:home')
