from django.shortcuts import render


def index(request, template_name='index.html'):
    user = request.user
    return render(request, template_name, {'username': user})
