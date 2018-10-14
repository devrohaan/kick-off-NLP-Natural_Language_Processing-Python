#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 22:16:27 2018

@author: Rohan

"""
from nltk import word_tokenize, sent_tokenize
import pickle

############################################################################

def tokenizeOnWhiteSpace(dataset):
    
    new_dataset = list()
    for story in dataset:
        
        new_dataset.append(story.split())
        
    return new_dataset




def tokenizeNLTKWord(dataset):
    
    new_dataset = list()
    for story in dataset:
        
        new_dataset.append(word_tokenize(story))
        
    return new_dataset


def tokenizeNLTKSentence(dataset):
    
    new_dataset = list()
    for story in dataset:
        
        new_dataset.append(sent_tokenize(story))
        
    return new_dataset



######################## Stopword removal ##################################

from stop_words import get_stop_words
from collections import deque

pypi_stopwords = get_stop_words('en')




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


def removeNoiseSWR2(words): #winner
    
    stop_words_set = set(stop_words)
    stop_words_set.update(['.', ',', '"', "'", '?', '!','’','‘'])
    #stop_words_set.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) # better do regex to cleanup.
    
    list_of_words = []
    for wordlist in words:
        list_of_words.append(list(set([word.lower() for word in wordlist]) - set(stop_words_set)))

    return list_of_words

def removeNoiseSWR1(words):
    
    stop_words_set = set(stop_words)
    stop_words_set.update(['.', ',', '"', "'", '?', '!','’','‘'])
    #stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) # better do regex to cleanup.
    
    list_of_words = []
    for wordlist in words:
        list_of_words.append([word.lower() for word in wordlist if word.lower() not in stop_words_set])

    return list_of_words

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

####################### Punctuation Removal ########################
    
"""Regex to remove punctuation from list of tokenized words"""

import re
import sys

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
    list_of_words = []
    for wordlist in words:
        wordlist = [word.translate(tbl) for word in wordlist]
        list_of_words.append(wordlist)
    
    return list_of_words

def removePunctuation4(text):
    
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

def preprocess_word(word):
    # Remove punctuation
    word = word.strip('\'"?!,.():;')
    # Convert more than 2 letter repetitions to 2 letter
    # funnnnny --> funny
    word = re.sub(r'(.)\1+', r'\1\1', word)
    # Remove - & '
    word = re.sub(r'(-|\')', '', word)
    return word


def is_valid_word(word):
    # Check if word begins with an alphabet
    return (re.search(r'^[a-zA-Z][a-z0-9A-Z\._]*$', word) is not None)


def handle_emojis(tweet):
    # Smile -- :), : ), :-), (:, ( :, (-:, :')
    tweet = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\))', ' EMO_POS ', tweet)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D
    tweet = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', ' EMO_POS ', tweet)
    # Love -- <3, :*
    tweet = re.sub(r'(<3|:\*)', ' EMO_POS ', tweet)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
    tweet = re.sub(r'(;-?\)|;-?D|\(-?;)', ' EMO_POS ', tweet)
    # Sad -- :-(, : (, :(, ):, )-:
    tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:)', ' EMO_NEG ', tweet)
    # Cry -- :,(, :'(, :"(
    tweet = re.sub(r'(:,\(|:\'\(|:"\()', ' EMO_NEG ', tweet)
    return tweet


def preprocess_tweet(tweet):
    #processed_tweet = []
    # Convert to lower case
    tweet = tweet.lower()
    # Replaces URLs with the word URL
    tweet = re.sub(r'((www\.[\S]+)|(https?://[\S]+))', ' URL ', tweet)
    # Replace @handle with the word USER_MENTION
    tweet = re.sub(r'@[\S]+', 'USER_MENTION', tweet)
    # Replaces #hashtag with hashtag
    tweet = re.sub(r'#(\S+)', r' \1 ', tweet)
    # Remove RT (retweet)
    tweet = re.sub(r'\brt\b', '', tweet)
    # Replace 2+ dots with space
    tweet = re.sub(r'\.{2,}', ' ', tweet)
    # Strip space, " and ' from tweet
    tweet = tweet.strip(' "\'')
    # Replace emojis with either EMO_POS or EMO_NEG
    tweet = handle_emojis(tweet)
    # Replace multiple spaces with a single space
    tweet = re.sub(r'\s+', ' ', tweet)
    
    

def normalizeDataset(dataset):
    
    cleaned_data = list()
    for story in dataset:
        cleaned_data.append(removePunctuation4(story))
    
    print(cleaned_data[0])
    cleaned_data = tokenizeNLTKWord(cleaned_data)
    cleaned_data = removeNoiseSWR2(cleaned_data)
    
    return cleaned_data


dataset = list()
with open('/Users/Rohan/Desktop/3rdAug/NLP/data/Story.pkl', 'rb') as handle:
    
    dataset = pickle.load(handle)
    
list_of_words = normalizeDataset(dataset)
with open("/Users/Rohan/Desktop/3rdAug/NLP/data/NoiseFreeWordList.pkl", "wb") as f:
    pickle.dump(list_of_words, f, protocol=pickle.HIGHEST_PROTOCOL)


