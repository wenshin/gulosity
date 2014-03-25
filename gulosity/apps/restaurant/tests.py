from django.test import TestCase
from django.contrib.auth.models import User

from models import RealUser


class TestAddRestaurant(TestCase):
    def setUp(self):
        from random import random
        username = str(random())[2:8]
        self.user = User.objects.create(username, '123456')

    def tearDown(self):
        self.user.delete()

    def test_real_user(self):
        identity = '123456789012343456'
        ru = RealUser(user=self.user, identity=identity)
        ru.save()