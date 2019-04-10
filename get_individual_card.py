import os
import time
import re
import csv
import requests
from pathlib import Path

from bs4 import BeautifulSoup, Comment


class GetCardsFromList:
    def __init__(self):
        pass

    @staticmethod
    def get_individual_cards_from_list():
        # Load list from csv
        load_file_directory = Path("expansion")
        load_file_name = Path("individual_url_list.csv")
        time_sleep = 6

        with open(load_file_directory / load_file_name, "r", encoding="utf8") as f:
            reader = csv.reader(f)

            # skip header
            next(reader)

            # get individual cards
            for title, url in reader:
                # get cards list for each expansions
                print(title, url)
                list_cards_in_expansions = GetCardsFromList.get_card_list_from_url(url)
                # get cards from list
                for card_url in list_cards_in_expansions:
                    title = card_url["title"]
                    url = card_url["url"]
                    print(title, url)
                    GetCardsFromList.fetch_individual_card_from_url(title=title, url=url)

                    # sleep
                    time.sleep(time_sleep)
            print("Complete")

    @staticmethod
    def fetch_individual_card_from_url(title: str, url: str, skip_exist_file=True) -> str or None:
        save_directory = Path("card")
        save_filename = Path(title.replace("/", "_"))

        # skip if file already exists
        if os.path.exists(save_directory / save_filename) and skip_exist_file:
            return None

        # open text
        with open(save_directory / save_filename, "w", encoding="utf8") as f:
            # get html
            response = requests.get(url)
            if response.status_code != 200:
                raise requests.HTTPError

            html = response.text
            soup = BeautifulSoup(html, "html.parser")

            # remove nav
            header = soup.find("h3", attrs={"id": "siteSub"})
            if header is not None:
                header.decompose()
            header = soup.find("div", attrs={"id": "jump-to-nav"})
            if header is not None:
                header.decompose()

            # remove footer
            for footer in soup.find_all("div", attrs={"id": "editsection"}):
                footer.decompose()
            for footer in soup.find_all("span", attrs={"class": "editsection"}):
                footer.decompose()
            for footer in soup.find_all("div", attrs={"class": "printfooter"}):
                footer.decompose()
            for footer in soup.find_all("div", attrs={"id": "ad_bottom"}):
                footer.decompose()

            # remove comment
            for comment in soup(text=lambda x: isinstance(x, Comment)):
                comment.extract()

            # extract text
            eval_text = soup.find("div", attrs={"id": "content"})
            pattern_text = "\n+"
            pattern_replace = "\n"
            pretty_text = re.sub(pattern_text, pattern_replace, eval_text.text.strip())
            pretty_text = re.sub("\n ", "\n", pretty_text)
            f.write(pretty_text)

            return pretty_text

    @staticmethod
    def get_card_list_from_url(url: str) -> list:
        domain = "http://www.mtgwiki.com"

        response = requests.get(url)
        if response.status_code != 200:
            raise requests.HTTPError

        html = response.text
        # find link to card
        soup = BeautifulSoup(html, "html.parser")

        # remove footer
        for i in range(3):
            footer = soup.find("a", attrs={"title": re.compile(".*カード個別評価.*")})
            if footer is not None:
                footer.decompose()
        footer = soup.find("div", attrs={"class": "printfooter"}).decompose()
        if footer is not None:
            footer.decompose()
        footer = soup.find("div", attrs={"id": "column-one"}).decompose()
        if footer is not None:
            footer.decompose()
        footer = soup.find("ul", attrs={"id": "f-list"}).decompose()
        if footer is not None:
            footer.decompose()

        # get links
        result = []
        list_tag = soup.find_all("li")
        for li in list_tag:
            selected_tag = li.find("a", attrs={"href": re.compile(".*wiki.*")})
            if selected_tag is not None:
                result_dic = {"title": selected_tag.text, "url": domain + selected_tag["href"]}
                result.append(result_dic)

        return result
