# -*- coding: utf-8 -*-


"""         
            N-Grams as Features:  

A combination of N words together are called N-Grams. 
N grams (N > 1) are generally more informative as compared to words (Unigrams) as features. 
Also, bigrams (N = 2) are considered as the most important features of all the others. 
The following code generates bigram of a text.
"""

def generate_ngrams(text, n):
    words = text.split()
    output = []  
    for i in range(len(words)-n+1):
        output.append(words[i:i+n])
    return output

print(generate_ngrams("The GoogleNews vector set is just word-vectors – not a full Word2Vec model. It doesn't have the full model internal weights that would be necessary for things like performing additional incremental training/predictions. That's why it should generally be loaded as a read-only KeyedVectors with limited functionality.", 2))

"""
    OP:
        
[['The', 'GoogleNews'], ['GoogleNews', 'vector'], ['vector', 'set'], ['set', 'is'], ['is', 'just'],
 ['just', 'word-vectors'], ['word-vectors', '–'], ['–', 'not'], ['not', 'a'], ['a', 'full'],
 ['full', 'Word2Vec'], ['Word2Vec', 'model.'], ['model.', 'It'], ['It', "doesn't"], ["doesn't", 'have'],
 ['have', 'the'], ['the', 'full'], ['full', 'model'], ['model', 'internal'], ['internal', 'weights'],
 ['weights', 'that'], ['that', 'would'], ['would', 'be'], ['be', 'necessary'], ['necessary', 'for'], 
 ['for', 'things'], ['things', 'like'], ['like', 'performing'], ['performing', 'additional'],
 ['additional', 'incremental'], ['incremental', 'training/predictions.'], ['training/predictions.', "That's"]
 , ["That's", 'why'], ['why', 'it'], ['it', 'should'], ['should', 'generally'], ['generally', 'be'],
 ['be', 'loaded'], ['loaded', 'as'], ['as', 'a'], ['a', 'read-only'], ['read-only', 'KeyedVectors'],
 ['KeyedVectors', 'with'], ['with', 'limited'], ['limited', 'functionality.']]

"""

