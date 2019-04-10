import fasttext
import gensim

if __name__ == '__main__':
    m = gensim.models.KeyedVectors.load_word2vec_format('./model.vec')
    print(m.most_similar('白'))

