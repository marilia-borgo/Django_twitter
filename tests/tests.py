from django.test import TestCase
from django.urls import reverse


def test_qualquer_coisa():
    pass


class LoginURLsTest(TestCase):
    def test_login_home_url_is_correct(self):
        login_url = reverse('login')
        self.assertEqual(login_url, '/login/')
