from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from models import RealUser


# @login_required
def index(request, template_name='index.html'):
    user = request.user
    return render(request, template_name, {'username': user})


def register(request, template_name=None):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, template_name, {
        'form': form,
    })


def logout(request, redirect_field_name=REDIRECT_FIELD_NAME):
    next_page = request.GET.get(redirect_field_name, '/')
    return auth_logout(request, next_page=next_page)


@login_required
def real_auth(request, template_name='real_auth.html'):
    user = request.user
    if request.method == 'POST':
        real_user = RealUser(user=user)
        form = real_user.get_form(data=request.POST)
        # form = RealUserForm(data=request.POST, instance=real_user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        # form = RealUserForm()
        form = RealUser.get_unbound_form()
    return render(request, template_name, {
        'user': user,
        'form': form
    })