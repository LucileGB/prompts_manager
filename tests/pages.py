import sys
import unittest

sys.path.append('../app')
from app import app


class TestPages(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_home(self):
        home = self.app.get('/')
        self.assertIn(b'Home', home.data)
        self.assertEqual(200, home.status_code)

    def test_prompts_list(self):
        prompts = self.app.get('/prompts')
        self.assertIn(b'Your Prompts', prompts.data)
        self.assertEqual(200, prompts.status_code)

if __name__ == '__main__':
    unittest.main()
