import re
import csv
from pathlib import  Path
from urllib import request
from bs4 import BeautifulSoup


class GetCardsList:
    def __init__(self):
        pass

    @staticmethod
    def get_cards_list():
        domain = "http://www.mtgwiki.com"
        url = domain + "/wiki/%E3%82%AB%E3%83%BC%E3%83%89%E5%80%8B%E5%88%A5%E8%A9%95%E4%BE%A1"
        file_directory = Path("expansion")
        file_name = Path("individual_url_list.csv")
        html = request.urlopen(url)

        soup = BeautifulSoup(html, "html.parser")
        url_list = soup.find_all("a", attrs={"title": re.compile("カード個別評価*")})

        with open(file_directory / file_name, "w", encoding="utf8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["title", "url"])
            for url in url_list:
                row = [url.get("title"), domain + url.get("href")]
                print(row)
                writer.writerow(row)
