from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def login(request):

        #return HttpResponseRedirect('home/')

        return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request, username = None):
    if username == request.user.username:
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                #messages.success(request, f'Info updated!')
                return redirect(f'/profile/{request.user.username}')
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

            user_list = User.objects.values()
            context = {
            'u_form' : u_form,
            'p_form' : p_form,
            'profile_owner' : request.user
            }
    elif username != request.user.username and username:
        context = {'profile_owner' : User.objects.filter(username=f'{username}').first()}
    else:
        return redirect(f'/profile/{request.user.username}')

    return render(request, 'users/profile.html', context)


def make_friends(request, operation, user_id):
    if operation == 'add':
        request.user.profile.friends.add(user_id)
    elif operation == 'rm':
        request.user.profile.friends.remove(user_id)
    return redirect(f'/profile/{User.objects.filter(id=user_id).first().username}')
