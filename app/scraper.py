import requests

from bs4 import BeautifulSoup


class AO3Formatter:
    """
    Format prompts scraped from AO3.
    """
    @staticmethod
    def clean_h3(title):
        """
        Take a fandom (h3) title and clean it.
        """
        title = title.text.strip()
        title = title.split("\n")[0]
        return title

    @staticmethod
    def format_list(items):
        """
        Clean a list of prompts and return it as a list.
        """
        items = items.text.strip().split("\n")
        return [item for item in items if len(item) > 0]

    @staticmethod
    def format_prompts(items):
        """
        Get a list of bs4's li tags and make it into strings.
        """
        return [item.text for item in items]

    @staticmethod
    def prepare_prompts(titles, prompts):
        """
        Take a list of titles, a list of prompts lists,
        and make them into dictonaries.
        
        Format: {'Fantasy': ['prompt', 'prompt', 'prompt'],
                'Mystery': ['prompt', 'prompt', 'prompt']}
        """
        result_dict = {}
        datas = list(zip(titles, prompts))

        for data in datas:
            result_dict.update({data[0]: data[1]})

        return result_dict


class TagSetScraper:
    """
    Scrape prompts from AO3's tagsets.
    """
    def __init__(self, url):
        self.formatter = AO3Formatter()
        self.url = url
    
    @property
    def soup(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, 'lxml')

    def original_h3(self, tag):
        return tag.name=='h3' and 'Original Work' in tag.contents[0]

    def get_original(self):
        """
        For multi-fandoms (= categories) exchanges, where we're only interested
        in the "original" category.
        """
        get_original_h3 = self.soup.find_all(self.original_h3)
        original_h3 = get_original_h3[0]

        prompts_ol = original_h3.findNext('ol')
        all_li = prompts_ol.find_all("li")

        return self.formatter.format_prompts(all_li)

    def get_fandoms_original(self):
        """
        NOT YET IMPLEMENTED.
        For original-only exchanges, where we only have to get all "fandoms".
        If everything is cleanly organized in fandoms, we format info
        life such.
        """
        cat = self.soup.find(id='list_for_media_Uncategorized_Fandoms')

        titles = cat.find_all(class_="expander_parent heading")
        titles = [self.formatter.clean_h3(title) for title in titles]
        prompts = cat.find_all(class_="tags index group commas")
        prompts = [self.formatter.format_list(items) for items in prompts]

        return self.formatter.prepare_prompts(titles, prompts)