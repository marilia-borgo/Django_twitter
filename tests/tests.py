from django.test import TestCase
from django.urls import reverse


def test_qualquer_coisa():
    pass


class LoginURLsTest(TestCase):
    def test_login_home_url_is_correct(self):
        url = reverse('login')
        self.assertEqual(url, '/login/')


class PostURLsTest(TestCase):
    def test_post_postDetail_url_is_correct(self):
        url = reverse('post_detail', kwargs={'pk': 19})
        self.assertEqual(url, '/logado/logado/19/')
