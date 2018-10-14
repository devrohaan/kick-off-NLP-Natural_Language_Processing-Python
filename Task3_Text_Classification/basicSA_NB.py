#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 23:21:30 2018

@author: Rohan
"""


from nltk.classify import NaiveBayesClassifier

def createBoWFastMethod(corpus):
   
    wordsSet = list(set(corpus))
    return dict([ (wordsSet[i], i) for i in range(len(wordsSet)) ])

def word2feats(word,bow):
    return dict([(key,True) if key == word else (key,False) for key, value in bow.items()])
 
positive_vocab = [ 'awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)' ]
negative_vocab = [ 'bad', 'terrible','useless', 'hate', ':(' ]
neutral_vocab = [ 'movie','the','sound','was','is','actors','did','know','words','not' ]
 
corpus = positive_vocab + negative_vocab + neutral_vocab

bow = createBoWFastMethod(corpus)

positive_features = [(word2feats(word,bow), 'pos') for word in positive_vocab]
negative_features = [(word2feats(word,bow), 'neg') for word in negative_vocab]
neutral_features = [(word2feats(word,bow), 'neu') for word in neutral_vocab]
 
train_set = negative_features + positive_features + neutral_features
 
classifier = NaiveBayesClassifier.train(train_set) 
 
# Predict
neg = 0
pos = 0
sentence = "outstanding hate bad bad bad terrific movie I it"
sentence = sentence.lower()
words = sentence.split(' ')
for word in words:
    classResult = classifier.classify(word2feats(word,bow))
    print(classResult)
    if classResult == 'neg':
        neg = neg + 1
    if classResult == 'pos':
        pos = pos + 1
 
print('Positive: ' + str(float(pos)/len(words)))
print('Negative: ' + str(float(neg)/len(words)))
