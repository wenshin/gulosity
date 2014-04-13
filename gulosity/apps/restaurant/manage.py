#!/usr/bin/env
# coding: utf-8


class RestaurantManager(object):
    def __init__(self, user):
        self.user = user

    def get_restaurant(self, slug):
        return Restaurant.objects.filter(slug_iexec=slug)

    def update(self):
        pass