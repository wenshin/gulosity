from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from gulosity.apps.accounts.models import UserPrivacy

from models import RestaurantPublic
from gulosity.libs.decorators import need_real_auth


def index(request):
    restaurants = RestaurantPublic.objects.all()
    return render(request, 'restaurant/index.html', {
        'user': request.user,
        'restaurants': restaurants
    })


def page(request, slug):
    user = request.user,
    restaurant = get_object_or_404(RestaurantPublic, slug=slug)
    if restaurant.is_owned_by(user):
        return render(request, 'restaurant/owner_page.html', {
            'slug': slug,
            'user': user,
            'restaurant': restaurant
        })
    else:
        return redirect('restaurant-new')


@login_required
@need_real_auth
def new(request):
    user = request.user
    if request.method == 'POST':
        user_private = UserPrivacy.objects.get(user=request.user)
        form = RestaurantPublic(owner=user_private).get_form(request.POST)
        if form.is_valid():
            r = form.save()
            if r:
                return redirect('restaurant-page', slug=r.slug)
    else:
        form = RestaurantPublic.get_unbound_form()
    return render(request, 'restaurant/new.html', {
        'user': user,
        'form': form
    })
