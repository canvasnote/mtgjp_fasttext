import time
import re
import csv
import requests
from pathlib import  Path

from bs4 import BeautifulSoup


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
                    # fetch_individual_card_from_url()

                    # sleep
                    time.sleep(time_sleep)

    @staticmethod
    def fetch_individual_card_from_url(title: str, url: str) -> None:
        save_filename = title.replace("/", "_")
        # open text
        with open(save_filename, "w"):
            pass

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
