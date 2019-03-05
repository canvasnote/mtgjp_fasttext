from pathlib import Path
import glob
from janome.tokenizer import Tokenizer


class Wakati:
    def __init__(self):
        self.tokenizer = Tokenizer()

    def wakati_all_file(self):
        source_directory = Path("card")
        target_directory = Path("card_wakati")
        file_list = glob.glob(str(source_directory) + "/*")
        for file in file_list:
            destination = target_directory / Path(file).name
            self.wakati_a_file(source=file, destination=destination)

    def wakati_a_file(self, source, destination):
        tokenizer = self.tokenizer
        with open(source, "r", encoding="utf8") as f_read:
            with open(destination, "w", encoding="utf8") as f_write:
                for row in f_read:
                    result = [token for token in tokenizer.tokenize(row, wakati=True)]
                    f_write.write(" ".join(result) + "\n")
