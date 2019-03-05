import  unittest
import  wakati


class TestWakati(unittest.TestCase):
    def test_wakati_all_file(self):
        w = wakati.Wakati()
        w.wakati_all_file()