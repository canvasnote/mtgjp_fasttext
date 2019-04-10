import glob
from pathlib import Path
import sys
import os
import io


class ConcatFiles:
    @staticmethod
    def concat_folder(path):
        path = Path(path)
        if not os.path.exists(path / Path('concat')):
            os.mkdir(path / Path('concat/'))
        with open(path / Path('concat/cards_concat'), mode='w', encoding='UTF8') as out_file:
            for in_file_name in glob.glob(str(path) + '/*'):
                print(in_file_name)
                if not os.path.isfile(in_file_name):
                    continue
                print('not directory')
                with open(in_file_name, mode='r', encoding='UTF8') as in_file:
                    for line in in_file.read():
                        out_file.write(line.replace('\n', ' '))
                    out_file.write('\n')



if __name__ == "__main__":
    ConcatFiles.concat_folder('card_wakati/')
