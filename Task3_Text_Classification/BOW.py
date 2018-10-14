#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 1 09:47:51 2018

@author: Rohan
"""

doc1 = """
Ronaldo was born in Portugal. He started playing soccer at a very young age
Ronaldo was born in Fundal
His full name is Cristiano Ronaldo Dos Santos Aveiro
The name Ronaldo in Cristiano Ronaldo was taken from the name of former Hollywood actor
"""

doc2 = """
The Earth was formed about 4.7 billion years ago.
The Earth shape is very close to that of a sphere
The Earth equatorial diameter is about 12756 km
The Earth rotates on its axis
"""      

corpus = [doc1, doc2]

def createBoWFastMethod(corpus):
    
    wordsSet = list(set(corpus[0].split()).union(set(corpus[1].split())))
    return dict([ (wordsSet[i], i) for i in range(len(wordsSet)) ])

bowFM = createBoWFastMethod(corpus)

def createBoW(corpus):
    
    bag_of_words = {}
    word_count = 0
    for sentence in corpus:
        for word in sentence.split():
            if word not in bag_of_words: # Unique words since its a vocab!
                bag_of_words[word] = word_count #set indexes
                word_count+=1
            
    return bag_of_words #index of words



def extraxtFeature(doc,bag_of_words):
    
    tokenSentence = doc.split()
    feture = [0 for x in range(len(bag_of_words))]
 
    for word in tokenSentence:
        index = bag_of_words[word]
        feture[index] +=1    # number of times the word has occured in the setence.
    
    return feture


bow = createBoW(corpus)

featureList = []
for doc in corpus:
    featureList.append(extraxtFeature(doc,bow))

print(featureList)
"""
from collections import Counter
wordsDictDoc1 = Counter(doc1.split())
print(wordsDictDoc1)
"""
  
 
    
