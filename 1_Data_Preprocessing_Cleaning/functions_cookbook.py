#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 22:16:27 2018

@author: Rohan

cookbook.py

data nikal
and normalise call kar

"""

import pickle
import sys
import inflect


dataset = list()
with open('/Users/Rohan/Desktop/3rdAug/NLP/data/Story.pkl', 'rb') as handle:
    
    dataset = pickle.load(handle)
            


# 1. Removing StopWords

# NLTK Stopwords
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

nltl_stopwords = stopwords.words("english")
type(nltl_stopwords) # list
print(len(nltl_stopwords)) # 179

for i in nltl_stopwords:
    print("".join(i), end = ", ")

"""
i, me, my, myself, we, our, ours, ourselves, you, you're, you've, you'll, you'd, your, yours, 
yourself, yourselves, he, him, his, himself, she, she's, her, hers, herself, it, it's, its, 
itself, they, them, their, theirs, themselves, what, which, who, whom, this, that, that'll, t
hese, those, am, is, are, was, were, be, been, being, have, has, had, having, do, does, did, 
doing, a, an, the, and, but, if, or, because, as, until, while, of, at, by, for, with, about, 
against, between, into, through, during, before, after, above, below, to, from, up, down, in, out, on, 
off, over, under, again, further, then, once, here, there, when, where, why, how, all, any, both, each, 
few, more, most, other, some, such, no, nor, not, only, own, same, so, than, too, very, s, t, can, will, 
just, don, don't, should, should've, now, d, ll, m, o, re, ve, y, ain, aren, aren't, couldn, couldn't, 
didn, didn't, doesn, doesn't, hadn, hadn't, hasn, hasn't, haven, haven't, isn, isn't, ma, mightn, 
mightn't, mustn, mustn't, needn, needn't, shan, shan't, shouldn, shouldn't, wasn, wasn't, weren, 
weren't, won, won't, wouldn, wouldn't,

"""

# http://pypi.python.org/pypi/stop-words

# pip install stopwords
 

from stop_words import get_stop_words

pypi_stopwords = get_stop_words('en')

print(len(pypi_stopwords)) # 174


# self defined stopwords


stop_words =['i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself',
            'yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself',
            'they','them','their','theirs','themselves','what','which','who','whom','this','that',
            'these','those','am','is','are','was','were','be','been','being','have','has','had',
            'having','do','does','did','doing','a','an','the','and','but','if','or','because','as',
            'until','while','of','at','by','for','with','about','against','between','into','through',
            'during','before','after','above','below','to','from','up','down','in','out','on','off',
            'over','under','again','further','then','once','here','there','when','where','why','how',
            'all','any','both','each','few','more','most','other','some','such','no','nor','not',
            'only','own','same','so','than','too','very','s','t','can','will','just','don','should',
            'now','uses','use','using','used','one','also']


stop_words_set = set(stop_words)



def tokenizeOnWhiteSpace(dataset):
    
    new_dataset = list()
    for story in dataset:
        
        new_dataset.append(story.split())
        
    return new_dataset

from nltk import word_tokenize, sent_tokenize

def tokenizeNLTKWord(dataset):
    
    new_dataset = list()
    for story in dataset:
        
        new_dataset.append(nltk.word_tokenize(story))
        
    return new_dataset

def tokenizeNLTKSentence(dataset):
    
    new_dataset = list()
    for story in dataset:
        
        new_dataset.append(nltk.sent_tokenize(story))
        
    return new_dataset

def removeNoiseSWR1(words):
    
    stop_words_set = set(stop_words)
    stop_words_set.update(['.', ',', '"', "'", '?', '!','’','‘'])
    #stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) # better do regex to cleanup.
    
    list_of_words = []
    for wordlist in words:
        list_of_words.append([word.lower() for word in wordlist if word.lower() not in stop_words_set])

    return list_of_words


def removeNoiseSWR2(words): #winner
    
    stop_words_set = set(stop_words)
    stop_words_set.update(['.', ',', '"', "'", '?', '!','’','‘'])
    #stop_words_set.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) # better do regex to cleanup.
    
    list_of_words = []
    for wordlist in words:
        list_of_words.append(list(set(wordlist) - set(stop_words_set)))

    return list_of_words

from collections import deque

def removeNoiseSWR3(words):
    
    stop_words_set = set(stop_words)
    stop_words_set.update(['.', ',', '"', "'", '?', '!','’','‘'])
    stopwordslist = deque(stop_words_set)
    
    list_of_words = []
    for wordlist in words:
        wordlist = set(wordlist)
        wordlist = deque(wordlist)
        list_of_words.append([word for word in wordlist if word not in stopwordslist])
    
    return list_of_words


"""Regex to remove punctuation from list of tokenized words"""
import re

def removePunctuation(words): #improve this not working
   
    
    list_of_words = []
    for wordlist in words:
        wordlist = re.sub(r'[^\w\s]', '', wordlist)
        list_of_words.append(wordlist)
    
    return list_of_words

def removePunctuation2(words): 
   
    
    puncts = ['.', ',', '"', "'", '?', '!','’','‘']
    list_of_words = []
    for wordlist in words:
        wordlist = [word for word in wordlist if word not in puncts]
        list_of_words.append(wordlist)
    
    return list_of_words

import string, unicodedata

def removePunctuation3(words): # replaces ',' with '' so not useful
   
    tbl = dict.fromkeys(i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P'))
    for wordlist in words:
        wordlist = [word.translate(tbl) for word in wordlist]
        list_of_words.append(wordlist)
    
    return list_of_words

def removePunctuation4(text):
    
    
    #table = str.maketrans('', '', string.punctuation)
    table = str.maketrans({key: None for key in string.punctuation})
    text = text.translate(table)
    return text

def remove_non_ascii(words):
    
    list_of_words = []
    for wordlist in words:
        wordlist = [unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore') for word in wordlist]
        list_of_words.append(wordlist)
    return list_of_words




from nltk.tokenize import RegexpTokenizer
def tokenizeNLTKNoPunct(dataset):
    
    tokenizer = RegexpTokenizer(r'\w+')
    new_dataset = list()
    for story in dataset:
        
        new_dataset.append(tokenizer.tokenize(story))
        # '‘', '‘' not removed
    return new_dataset

########### Text Standardization: Removing Slangs and typos############
    
lookup_dict = {
    'awsm':'awesome',
    'lol' : 'laughing out loud',
    'brb':'be right back',
    'btw':'by the way',
    'lmk':'let me know',
    'g2g':'got to go',
    'rt':'retweet',
    'dm':'direct message',
    "awsm" : "awesome",
    "luv" :"love"}

def Standardize(input_text):
    words = input_text.split() 
    new_words = []
    for word in words:
        if word.lower() in lookup_dict:
            word = lookup_dict[word.lower()]
            new_words.append(word)
        else:
            new_words.append(word)
    return " ".join(new_words)

print(Standardize("Input"))

######### Remove HTML parser. ###############




def unescape(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    s = s.replace("&amp;", "&")
    return s

# alternative
    
import html
html.unescape("Input")

################## Expanding Apostrophe  #########

dictApost = {
    "'s" : " is",
    "you're" : "you are",
    "u're" : "you are",
    "can't" : " cannot",
    "won't" : " will not", 
    "isn't" : " is not", 
    "it's" : " it is", 
    "o'clock" : " of the clock"
} ## Need a huge dictionary

words = "Text".split()
reformed = [dictApost[word] if word in dictApost else word for word in words]
inputTweet = " ".join(reformed)





 ######### Stemming and Lemmatization Difference  #########

import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer 
from nltk.stem import PorterStemmer 


stemmer = PorterStemmer() 
lemmatizer = WordNetLemmatizer() 

word = "multiplying" 
print(lemmatizer.lemmatize(word, "v"))
# "multiply" 
print(stemmer.stem(word))
# "multipli"


######################################
def normalizeDataset(dataset):
    pass

    
if __name__ == "__main__":
    
    data = tokenizeOnWhiteSpace(dataset)
    data = normalizeDataset(dataset)
    data = tokenizeNLTKWord(dataset)
    data = tokenizeNLTKSentence(dataset)
    

    list_of_words = removeNoiseSWR1(data)
    list_of_words = removeNoiseSWR2(data)
    list_of_words = removeNoiseSWR3(data)
    
    list_of_words = removePunctuation2(data) #best till now
    list_of_words = removePunctuation3(data)
    
    list_of_words = remove_non_ascii(data)
'''
pattern has no support for python3
from pattern.web import Twitter, plaintext

twitter = Twitter(language='en') 
for tweet in twitter.search('"more important than"', cached=False):
    print plaintext(tweet.text)
'''



