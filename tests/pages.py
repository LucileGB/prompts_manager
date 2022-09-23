import sys
import unittest

sys.path.append('../app')
from app import app


class TestGet(unittest.TestCase):
    def setUp(self):
        app.app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.app.test_client()

    def tearDown(self):
        self.app = None

    def test_home(self):
        home = self.app.get("/")
        self.assertIn(b"Home", home.data)
        self.assertEqual(200, home.status_code)

    def test_prompts_list(self):
        prompts = self.app.get("/prompts")
        self.assertIn(b"Your Prompts", prompts.data)
        self.assertEqual(200, prompts.status_code)


class TestPromptListTagsetForm(unittest.TestCase):
    def setUp(self):
        app.app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.app.test_client()

    def tearDown(self):
        self.app = None

    def test_prompts_list_post(self):
        user_input = {"url": "https://archiveofourown.org/tag_sets/10303"}
        prompts = self.app.post(
            "/prompts",
            data=user_input,
            follow_redirects=True
            )

        self.assertEqual(200, prompts.status_code)

    def test_prompts_list_post_empty_list(self):
        pass

    def test_prompts_list_post_invalid_url(self):
        pass


class TestPromptListPromptForm(unittest.TestCase):
    def setUp(self):
        app.app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.app.test_client()

    def tearDown(self):
        self.app = None

    def test_prompts_list_post(self):
        user_input = {"prompt": "A witty prompt"}
        prompts = self.app.post(
            "/prompts",
            data=user_input,
            follow_redirects=True
            )

        self.assertEqual(200, prompts.status_code)
        self.assertIn(b"A witty prompt", prompts.data)


if __name__ == '__main__':
    unittest.main()
