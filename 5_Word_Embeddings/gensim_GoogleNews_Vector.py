#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 23:03:43 2018

@author: Rohan
"""


from gensim.models.keyedvectors import KeyedVectors

word_vectors=KeyedVectors.load_word2vec_format('/Users/Rohan/Desktop/3rdAug/Heavydata/GoogleNews-vectors-negative300.bin',binary=True)

"""
Gensim allocates a big matrix to hold all of the word vectors, and if you do the math…
3 million words * 300 features * 4bytes/feature = ~3.35GB
.... that’s a big matrix!
"""

vocab = word_vectors.vocab.keys()
print(len(vocab)) # 3000000

#Similarity
print (word_vectors.similarity('Ronaldo', 'Messi')) # 0.8209548
print (word_vectors.similarity('fire', 'water')) # 0.22717671

#picking odd one out
print(word_vectors.doesnt_match("Ronaldo Messi Hamilton Sachin".split())) # Hamilton 

print(word_vectors.predict_output_word(['Sachin','Sehwag','Laxman','Dravid'], topn=10))


	
"""
The `GoogleNews` vector set is just word-vectors – not a full Word2Vec model. It doesn't have the full model internal weights that would be necessary for things like performing additional incremental training/predictions. That's why it should generally be loaded as a read-only `KeyedVectors` with limited functionality. 

To have a working `Word2Vec` model with full functionality, you'd need to train it yourself, or load a true full model (which would be in a different gensim-native disk format, and be loaded with the `load()` method). Google hasn't made the full model that created the `GoogleNews` vectors available.

The usual value/application of `Word2Vec` is *not* examining the model's word-predictions – and many word2vec implementations don't even offer an interface to calculate predictions separate from the training loops. Rather, Word2Vec uses the exercise of trying-to-predict (even if quite poorly) to bootstrap word-vectors that then fortunately become useful for other purposes.

best resource

https://radimrehurek.com/gensim/models/word2vec.html

"""


import pandas as pd
import gzip
 
def parse(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield eval(l)

def getDF(path):
    i = 0
    df = {}
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')
   

video_data = getDF('reviews_Amazon_Instant_Video_5.json.gz')


