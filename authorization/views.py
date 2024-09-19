from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserSettingsForm, NewLinkForm
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Link, User

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно зарегестрирован')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'authorization/registration.html', {'form': form})

def user_account(request):
    return render(request, 'authorization/user.html', {'data': len(Link.objects.filter(user=f'{request.user.id}'))})

def user_links(request):
    obj_id = request.GET.get('id')
    obj = Link.objects.filter(id=obj_id)
    obj.delete()
    
    data = {'links': Link.objects.filter(user=f'{request.user.id}')}
    return render(request, 'authorization/links.html', data)

def user_settings(request):
    if request.method == 'POST':
        settingsForm = UserSettingsForm(request.POST, instance=request.user)
        if settingsForm.is_valid():
            settingsForm.save()
            messages.success(request, 'Данные успешно обновлены')
            return redirect('user')
    else:
        settingsForm = UserSettingsForm(instance=request.user)
    
    return render(request, 'authorization/settings.html', {'settingsForm': settingsForm})

def user_newlink(request):
    if request.method == 'POST':
        newLinkForm = NewLinkForm(request.POST)
        if newLinkForm.is_valid():
            obj = newLinkForm.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Малинка успешна создана')
            return redirect('links')       
    else:
        newLinkForm = NewLinkForm()

    return render(request, 'authorization/newlink.html', {'newLinkForm': newLinkForm})