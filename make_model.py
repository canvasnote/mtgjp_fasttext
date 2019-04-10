
import fasttext as ft
import sys


def make_model(input_file, output_filename='model'):
    model = ft.skipgram(input_file, output_filename)
    print(model.words)


if __name__ == "__main__":

    make_model(input_file='./card_wakati/concat/cards_concat', output_filename='text_model')


