import os
import sys
import unittest

sys.path.append('../app')
from app import app, database


class TestPromptsHandling(unittest.TestCase):
    def setUp(self):
        app.app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.app.test_client()

        self.db = database.Database("test_db.db")
        prompts = ["Amateur Sleuth Who Sees Ghosts & Person Whose Death...",
                    "Big Bad Villain & Plucky Young Chosen One (OW)",
                    "Brilliant But Socially Awkward Male Inventor &...",
                    "Chosen One & Former Chosen One Who is Now Retired",
                    "Disabled Male Veteran of Magical War & Trauma...",
            ]
        self.db.create_prompt_list(prompts)

    def tearDown(self):
        self.app = None
        os.remove("test_db.db")

    def test_delete_prompt(self):
        user_input = {"prompt": "A witty prompt"}
        prompts = self.app.post("/prompts",
            data=user_input,
            follow_redirects=True
            )

        self.assertEqual(200, prompts.status_code)
        self.assertIn(b"A witty prompt", prompts.data)

    def test_access_edit_page(self):
        user_input = {"prompt": "A witty prompt"}
        self.assertEqual(200, prompts.status_code)
        self.assertIn(b"A witty prompt", prompts.data)

    def test_edit_prompt(self):
        user_input = {"prompt": "A witty prompt"}
        prompts = self.app.post("/prompts",
            data=user_input,
            follow_redirects=True
            )

        self.assertEqual(200, prompts.status_code)
        self.assertIn(b"A witty prompt", prompts.data)

if __name__ == '__main__':
    unittest.main()