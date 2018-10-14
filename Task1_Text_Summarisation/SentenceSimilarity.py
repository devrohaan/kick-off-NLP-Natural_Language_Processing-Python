#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 02:12:48 2018
@author: Rohan
"""
from nltk.corpus import brown
from nltk.cluster.util import cosine_distance

from stop_words import get_stop_words
pypi_stopwords = get_stop_words('en')


"""
A widely used measure in Natural Language Processing is the Cosine Similarity. The Cosine Similarity computes the cosine of the angle between 2 vectors. If the vectors are identical, the cosine is 1.0. If the vectors are orthogonal, the cosine is 0.0. This means the cosine similarity is a measure we can use.

NLTK implements cosine_distance, which is 1 - cosine_similarity. The concept of distance is opposite to similarity. Two identical vectors are located at 0 distance and are 100% similar.


"""

def sentence_similarity(doc1, doc2, stopwords=None):
    
    
    doc1 = [word.lower() for word in doc1]
    doc2 = [word.lower() for word in doc2]
    worddict = list(set(doc1 + doc2) - set(pypi_stopwords))
    print(worddict)
    vec1 = [0] * len(worddict)
    vec2 = [0] * len(worddict)
    # build the vector for the first sentence
    for word in doc1:
        if word in pypi_stopwords:
            continue
        else:
            vec1[worddict.index(word)] += 1
    # build the vector for the second sentence
    for word in doc2:
        if word in pypi_stopwords:
            continue
        else:
            vec2[worddict.index(word)] += 1
    
    
    print(vec1)
    print(vec2)
    
    return 1 - cosine_distance(vec1, vec2)


# One out of 5 words differ => 0.8 similarity
print(sentence_similarity("This is a good sentence".split(), "This is a bad sentence".split()))
# One out of 2 non-stop words differ => 0.5 similarity
print(sentence_similarity("This is a good sentence".split(), "This is a bad sentence".split(), stopwords.words('english')))
# 0 out of 2 non-stop words differ => 1 similarity (identical sentences)
print(sentence_similarity("This is a good sentence".split(), "This is a good sentence".split(), stopwords.words('english')))
# Completely different sentences=> 0.0
print(sentence_similarity("This is a good sentence".split(), "I want to go to the market".split(), stopwords.words('english')))



import math
from collections import Counter
def get_cosine(vec1, vec2):
    common = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in common])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()]) 
    sum2 = sum([vec2[x]**2 for x in vec2.keys()]) 
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
   
    if not denominator:
        return 0.0 
    else:
        return float(numerator) / denominator

def text_to_vector(text): 
    words = text.split() 
    return Counter(words)

text1 = 'This is an article on analytics vidhya' 
text2 = 'article on analytics vidhya is about natural language processing'

vector1 = text_to_vector(text1) 
vector2 = text_to_vector(text2) 
cosine = get_cosine(vector1, vector2)


