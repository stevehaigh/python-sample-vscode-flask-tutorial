import os
import unittest

from hello_app import app
from hello_app import views
 
class BasicTests(unittest.TestCase):
        
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        print("## Test setUp")
 
    def tearDown(self):
        print("## Test tearDown")

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_page_not_found(self):
        response = self.app.get('/foo/', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
 
if __name__ == "__main__":
    unittest.main()