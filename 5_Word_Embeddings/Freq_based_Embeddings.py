#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:53:44 2018

@author: Rohan
"""


import nltk 
import pickle


dataset = list()
with open('/Users/Rohan/git/NLP/data/NoiseFreeWordList.pkl', 'rb') as handle:
    dataset = pickle.load(handle)
            
print(dataset[0])
#tokens = [t for t in dataset[0].split()] 

allTokens = []

for wordlist in dataset:
    for word in wordlist:
        allTokens.append(word)
    
print("Length of Dict ", len(allTokens))
freq = nltk.FreqDist(allTokens) 
print(type(freq)) #'nltk.probability.FreqDist'
for key,val in freq.items(): 
    print (str(key) + ':' + str(val))
freq.plot(20, cumulative=False)

#OR

wordfreq = [allTokens.count(w) for w in allTokens]
print("Pairs\n", list(zip(allTokens, wordfreq)))


#Creating count matrix
# creating bag of words

"""
The bag-of-words model is one of the feature extraction algorithms for text.
The bag of words model ignores grammar and order of words.
"""



from collections import Counter
import pandas as pd
# Find all the unique words in the dataset.
allTokens = []

for wordlist in dataset:
    for word in wordlist:
        allTokens.append(word) #4042
        
unique_words = list(set(allTokens))
print("Length of Dict ", len(unique_words)) #1887

def make_matrix(dataset, vocab):
    
    """
    We are making bag of words model for all stories.
    """
    matrix = []
    for wordlist in dataset:
        # Count each word in the story, and make a dictionary.
        counter = Counter(wordlist)
        # Turn the dictionary into a matrix row using the vocab.
        row = [counter.get(w, 0) for w in vocab]
        matrix.append(row)
    df = pd.DataFrame(matrix)
    df.columns = unique_words
    return df

print(make_matrix(dataset, unique_words))


"""
Dataset has 56 stories, Thus 55 rows
unique_words count is 1887 column
Thus bag of words matrix is 55*1887
"""



############ TF_IDF  ##############3

from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
        "Cristaino Ronaldo was born in Portugal. He started playing soccer at a very young age, and over his career he has won many awards. Cristaino Ronaldo was born in Fundal, Portugal on February, 1985. His full name is Cristaino Ronaldo Dos Santos Aveiro.The name ‘Ronaldo’ in Cristaino Ronaldo was taken from the name of former Hollywood actor and ex-us President Ronald Reagan due to his father’s love and respect for Ronald Reagan.",
        "The Earth was formed about 4.7 billion years ago. The Earth’s shape is very close to that of a sphere, not perfectly spherical. The Earth’s equatorial diameter is about 12,756 km. The Earth rotates on its axis, an imaginary straight line through its centre. The two points where the axis of rotation intersects the Earth’s surface are called as the poles. The Earth rotates in counter-clock direction or from left to right-or eastward direction"
        ]
obj = TfidfVectorizer()

X = obj.fit_transform(corpus)
print(X[1])


"""
The model creates a vocabulary dictionary and assigns an index to each word. 
Each row in the output contains a tuple (i,j) and a tf-idf value of word at index j in document i.

Ronaldo
(0,1) =>

"""

