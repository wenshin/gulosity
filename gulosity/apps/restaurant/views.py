from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from gulosity.main.models import RealUser

from models import Restaurant
from forms import RestaurantFrom


def index(request, restaurant_name=None):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant/index.html', {
        'restaurants': restaurants
    })


@login_required
def add(request, template_name="restaurant/add.html"):
    user = request.user
    if request.method == 'POST':
        real_user = RealUser(user=user)
        form = Restaurant(owner=real_user).get_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Restaurant.get_unbound_form()
    return render(request, template_name, {
        'form': form
    })
