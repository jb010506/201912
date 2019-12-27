
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec

print("hi");

glove_file = datapath('/Users/william/Desktop/word2vec/glove.6B.100d.txt')
w2v_output_filename = "/Users/william/Desktop/word2vec/glove.6B.100d.txt.word2vec"
w2v_file = get_tmpfile(w2v_output_filename)
model = KeyedVectors.load_word2vec_format(w2v_file)

print("start")
a='y'
while a =='y':

    ques = input("enter a word: ")
    print("the most similar: ")
    try:
        print(model.most_similar(ques))
    except Exception:
        print("error")
    a = input("Continue? (y/n): ")
