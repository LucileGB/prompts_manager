import sys
import unittest

sys.path.append('../app')
from app import scraper


class TestScrape(unittest.TestCase):
    def test_right_amount_of_prompts(self):
        scrap = scraper.TagSetScraper(
            "https://archiveofourown.org/tag_sets/10303"
            )

        self.assertEqual(31, len(scrap.get_original()))

    def test_right_prompt_format(self):
        scrap = scraper.TagSetScraper(
            "https://archiveofourown.org/tag_sets/10303"
            )
        prompts = scrap.get_original()

        self.assertEqual(
            "Amateur Sleuth Who Sees Ghosts & Person Whose Death They're Investigating (OW)",
            prompts[0]
            )
