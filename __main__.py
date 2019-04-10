import argparse

import get_cards_list
import get_individual_card
import wakati
import concat_wakati
import make_model

if __name__ == "__main__":
    """
     usage:
     -l --list カード個別評価一覧のページからエキスパンション一覧を取得し、CSVに保存します。
     -g --get-cards カードリストCSVからカードの記事を取得し、CSVに保存します。
     -w, --wakati カードの情報を分かち書きにします。
     -h --help このヘルプを表示します。
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--list", action="store_true")
    parser.add_argument("-g", "--get-cards", action="store_true")
    parser.add_argument("-w", "--wakati", action="store_true")
    parser.add_argument("-c", "--concat-wakati", action="store_true")
    parser.add_argument("-m", "--make-model", action="store_true")
    # parser.add_argument("-h", "--help", help="このヘルプを表示します。")
    args = parser.parse_args()

    if args.list:
        get_cards_list.GetCardsList().get_cards_list()

    if args.get_cards:
        get_individual_card.GetCardsFromList().get_individual_cards_from_list()

    if args.wakati:
        w = wakati.Wakati()
        w.wakati_all_file()

    if args.concat_wakati:
        concat_wakati.ConcatFiles.concat_folder('card_wakati/')

    if args.make_model:
        make_model.MakeModel.make_model(input_file='./card_wakati/concat/cards_concat', output_filename='model')
