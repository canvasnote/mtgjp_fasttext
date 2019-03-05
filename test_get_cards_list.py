import os
import unittest
import csv
import re
import get_cards_list


class TestGetCardsList(unittest.TestCase):
    def test_get_cards_list(self):
        path = r"expansion/individual_url_list.csv"
        if os.path.exists(path):
            os.remove(path)

        get_cards_list.GetCardsList().get_cards_list()
        with open(path, "r", encoding="utf8") as f:
            reader = csv.reader(f)
            self.assertTrue(next(reader) == ["title", "url"])

            pattern_title = re.compile("カード個別評価")
            pattern_url = re.compile("http://www.mtgwiki.com/wiki/")
            for row in reader:
                self.assertTrue(pattern_title.match(row[0]))
                self.assertTrue(pattern_url.match(row[1]))
