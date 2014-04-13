#!/usr/bin/env
# coding: utf-8

from django.shortcuts import render

from gulosity.apps.restaurant.models import RestaurantPublic


def index(request):
    user = request.user
    if user.is_authenticated:
        my_restaurants = RestaurantPublic.get_my_restaurants(user)
        return render(request, 'main/user_index.html', {
            'username': user,
            'my_restaurants': my_restaurants,
        })
    else:
        return render(request, 'index.html', {'username': user})
