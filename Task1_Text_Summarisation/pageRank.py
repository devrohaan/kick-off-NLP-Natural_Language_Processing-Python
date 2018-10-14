#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 19:52:02 2018

@author: Rohan
"""
import numpy as np
nltk.download('brown')

links = {
    'webpage-1': set(['webpage-2', 'webpage-4', 'webpage-5', 'webpage-6', 'webpage-8', 'webpage-9', 'webpage-10']),
    'webpage-2': set(['webpage-5', 'webpage-6']),
    'webpage-3': set(['webpage-10']),
    'webpage-4': set(['webpage-9']),
    'webpage-5': set(['webpage-2', 'webpage-4']),
    'webpage-6': set([]), # dangling page
    'webpage-7': set(['webpage-1', 'webpage-3', 'webpage-4']),
    'webpage-8': set(['webpage-1']),
    'webpage-9': set(['webpage-1', 'webpage-2', 'webpage-3', 'webpage-8', 'webpage-10']),
    'webpage-10': set(['webpage-2', 'webpage-3', 'webpage-8', 'webpage-9']),
}

def build_index(links):
    website_list = links.keys()
    print(website_list)
    return {website: index for index, website in enumerate(website_list)}
 
website_index = build_index(links)
print(website_index)

 
def build_transition_matrix(links, index):
    total_links = 0
    A = np.zeros((len(index), len(index)))
    print(A)
    for webpage in links:
        # dangling page
        if not links[webpage]:
            # Assign equal probabilities to transition to all the other pages
            A[index[webpage]] = np.ones(len(index)) / len(index)
        else:
            for dest_webpage in links[webpage]:
                total_links += 1
                A[index[webpage]][index[dest_webpage]] = 1.0 / len(links[webpage])
 
    return A
 
A = build_transition_matrix(links, website_index)
print(A)


def pagerank(A, eps=0.0001, d=0.85):
    P = np.ones(len(A)) / len(A)
    while True:
        new_P = np.ones(len(A)) * (1 - d) / len(A) + d * A.T.dot(P)
        delta = abs(new_P - P).sum()
        if delta <= eps:
            return new_P
        P = new_P
 
results = pagerank(A)
 
print("Results:", results) # [ 0.13933698,  0.09044235,  0.1300934 ,  0.13148714,  0.08116465, 0.1305122 ,  0.09427366,  0.085402  ,  0.02301397,  0.09427366]
#print(sum(results)) # 1.0
print([item[0] for item in sorted(enumerate(results), key=lambda item: -item[1])]) # [0, 3, 5, 2, 6, 9, 1, 7, 4, 8]
 


from nltk.corpus import brown, stopwords
 
# Get a text from the Brown Corpus
sentences = brown.sents('ca01')
 
print(sentences)
# [[u'The', u'Fulton', u'County', u'Grand', u'Jury', u'said', u'Friday', u'an', u'investigation', u'of', u"Atlanta's", u'recent', u'primary', u'election', u'produced', u'``', u'no', u'evidence', u"''", u'that', u'any', u'irregularities', u'took', u'place', u'.'], [u'The', u'jury', u'further', u'said', u'in', u'term-end', u'presentments', u'that', u'the', u'City', u'Executive', u'Committee', u',', u'which', u'had', u'over-all', u'charge', u'of', u'the', u'election', u',', u'``', u'deserves', u'the', u'praise', u'and', u'thanks', u'of', u'the', u'City', u'of', u'Atlanta', u"''", u'for', u'the', u'manner', u'in', u'which', u'the', u'election', u'was', u'conducted', u'.'], ...]
 
print(len(sentences))  #  98
 
# get the english list of stopwords
stop_words = stopwords.words('english')
 

from nltk.cluster.util import cosine_distance
 
def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences, stopwords=None):
    # Create an empty similarity matrix
    S = np.zeros((len(sentences), len(sentences)))
 
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue
 
            S[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)
 
    # normalize the matrix row-wise
    for idx in range(len(S)):
        S[idx] /= S[idx].sum()
 
    return S
 
S = build_similarity_matrix(sentences, stop_words)    
print(S)


from operator import itemgetter 
 
sentence_ranks = pagerank(S)
 
print(sentence_ranks)
 
# Get the sentences ordered by rank
ranked_sentence_indexes = [item[0] for item in sorted(enumerate(sentence_ranks), key=lambda item: -item[1])]
print(ranked_sentence_indexes)
 
# Suppose we want the 5 most import sentences
SUMMARY_SIZE = 5
SELECTED_SENTENCES = sorted(ranked_sentence_indexes[:SUMMARY_SIZE])
print(SELECTED_SENTENCES)
 
# Fetch the most important sentences
summary = itemgetter(*SELECTED_SENTENCES)(sentences)
 
# Print the actual summary
for sentence in summary:
    print(' '.join(sentence))
    
    
    

