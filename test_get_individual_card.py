import unittest
import get_individual_card
import re


class TestGetCardsFromList(unittest.TestCase):
    def test_get_card_list_from_url(self):
        url = "http://www.mtgwiki.com/wiki/%E3%82%AB%E3%83%BC%E3%83%89%E5%80%8B%E5%88%A5%E8%A9%95%E4%BE%A1%EF%BC%9A%E3%83%89%E3%83%A9%E3%82%B4%E3%83%B3%E3%81%AE%E8%BF%B7%E8%B7%AF"

        result = (get_individual_card.GetCardsFromList.get_card_list_from_url(url))
        pattern = re.compile(r"http://www.mtgwiki.com/wiki/")

        for row in result:
            self.assertTrue(len(row["title"]) > 0)
            self.assertTrue(pattern.match(row["url"]))
