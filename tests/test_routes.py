from app import app
import unittest

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 302)

    def test_register(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.app.get('/profile')
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()