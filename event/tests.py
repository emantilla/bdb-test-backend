from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class EventTestCase(TestCase):
    def test_register(self):
        url = '/event/addUser/'
        response = self.client.post(url, {"password": "abcd1234","email": "testEmail@hotmail.com"}, content_type ="application/json")
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        # Create user
        user_model = User.objects.create_user(username="testEmail@hotmail.com", password="abcd1234")
        user_model.email = "testEmail@hotmail.com"
        user_model.save()
        
        # test login API
        url = '/event/login/'
        response = self.client.post(url, {"password": "abcd1234","email": "testEmail@hotmail.com"}, content_type ="application/json")
        self.assertEqual(response.status_code, 200)

    def test_login_error(self):
        # Create user
        user_model = User.objects.create_user(username="testEmail@hotmail.com", password="abcd1234")
        user_model.email = "testEmail@hotmail.com"
        user_model.save()
        
        # test login API
        url = '/event/login/'
        response = self.client.post(url, {"password": "abc","email": "testEmail@hotmail.com"}, content_type ="application/json")
        self.assertEqual(response.status_code, 401)