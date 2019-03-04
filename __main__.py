import argparse

import get_cards_list

if __name__ == "__main__":
    """
     usage:
     -l --list カード個別評価一覧のページからエキスパンション一覧を取得し、CSVに保存します。
     -g --get-cards カードリストCSVからカードの記事を取得し、CSVに保存します。
     -h --help このヘルプを表示します。
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--list", action="store_true")
    parser.add_argument("-g", "--get-cards", action="store_true")
    # parser.add_argument("-h", "--help", help="このヘルプを表示します。")
    args = parser.parse_args()

    if args.list:
        get_cards_list.GetCardsList()
