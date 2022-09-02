import os
import sys
import unittest

sys.path.append('../app')
from app import database


class TestGet(unittest.TestCase):
    def setUp(self):
        self.db = database.Database("test_db.db")
        prompts = ["Amateur Sleuth Who Sees Ghosts & Person Whose Death...",
                    "Big Bad Villain & Plucky Young Chosen One (OW)",
                    "Brilliant But Socially Awkward Male Inventor &...",
                    "Chosen One & Former Chosen One Who is Now Retired",
                    "Disabled Male Veteran of Magical War & Trauma...",
            ]
        self.db.create_prompt_list(prompts)

    def tearDown(self):
        os.remove("test_db.db")

    def test_input_is_sanitized(self):
        prompt = "DROP TABLE prompts;"
        self.db.create_prompt(prompt)
        prompts = self.db.get_prompts_list()

        self.assertEqual(len(prompts), 6)
        self.assertIn("DROP TABLE prompts;", prompts[5])

    def test_all_columns_are_here(self):
        prompts = self.db.get_prompts_list()
        self.assertEqual(
            ("Amateur Sleuth Who Sees Ghosts & Person Whose Death...", "null", 1),
            prompts[0]
            )

    def test_get_prompts_list_returns_everything(self):
        prompts = self.db.get_prompts_list()

        self.assertEqual(len(prompts), 5)
        self.assertIn("Amateur Sleuth Who Sees Ghosts & Person Whose Death...",
            prompts[0]
            )

    def test_input_is_sanitized(self):
        prompt = "DROP TABLE prompts;"
        self.db.create_prompt(prompt)
        prompts = self.db.get_prompts_list()

        self.assertEqual(len(prompts), 6)
        self.assertIn("DROP TABLE prompts;", prompts[5])

        self.db.edit_prompt_body("DROP TABLE prompts;", "DROP TABLE prompts;")
        prompts = self.db.get_prompts_list()
        self.assertEqual(len(prompts), 6)

    def test_prompt_creation(self):
        prompt = "A riveting idea"
        self.db.create_prompt(prompt)
        prompts = self.db.get_prompts_list()

        self.assertEqual(len(prompts), 6)
        self.assertIn("A riveting idea", prompts[5])

    def test_prompts_list_creation(self):
        prompt = "A riveting idea"
        self.db.create_prompt(prompt)
        prompts = self.db.get_prompts_list()

        self.assertEqual(len(prompts), 6)
        self.assertIn("A riveting idea", prompts[5])

    def test_duplicates_are_not_inserted(self):
        pass # test with list, then prompt here

    def test_delete_prompt(self):
        self.db.delete_prompt(1)
        prompts = self.db.get_prompts_list()

        self.assertEqual(len(prompts), 4)
        self.assertFalse(
            "Amateur Sleuth Who Sees Ghosts & Person Whose Death..." ==
            prompts[0][0])
        self.assertTrue(
            "Big Bad Villain & Plucky Young Chosen One (OW)" ==
            prompts[0][0])

    def test_edit_prompt_body(self):
        self.db.edit_prompt_body(1,
                            "Expert Sleuth Who Sees Living People & Person Whose Life...")
        prompts = self.db.get_prompts_list()

        self.assertEqual(len(prompts), 5)
        self.assertTrue(
            "Expert Sleuth Who Sees Living People & Person Whose Life..." ==
            prompts[0][0])

    def test_edit_prompt_collection(self):
        self.db.edit_prompt_collection("Amateur Sleuth Who Sees Ghosts & Person Whose Death...",
                            "Mystery")
        prompts = self.db.get_prompts_list()

        self.assertTrue(
            "Amateur Sleuth Who Sees Ghosts & Person Whose Death..." ==
            prompts[0][0])
        self.assertTrue(
            "Mystery" ==
            prompts[0][1])


if __name__ == '__main__':
    unittest.main()