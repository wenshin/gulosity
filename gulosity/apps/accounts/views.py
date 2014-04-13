from django.shortcuts import render, redirect
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from models import UserPrivacy


@login_required
def index(request):
    user = request.user
    return render(request, 'accounts/index.html', {
        'user': user
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {
        'form': form,
    })


def logout(request):
    next_page = request.GET.get(REDIRECT_FIELD_NAME, '/')
    return auth_logout(request, next_page=next_page)


@login_required
def real_auth(request):
    user = request.user
    if request.method == 'POST':
        user_private = UserPrivacy(user=user)
        form = user_private.get_form(data=request.POST)
        # form = UserPrivacyForm(data=request.POST, instance=user_private)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        # form = UserPrivacyForm()
        form = UserPrivacy.get_unbound_form()
    return render(request, 'accounts/real_auth.html', {
        'user': user,
        'form': form
    })
