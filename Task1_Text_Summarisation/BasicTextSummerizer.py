#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 12:36:08 2018

21984
@author: Rohan
"""
from nltk import sent_tokenize
from stop_words import get_stop_words
import string
from collections import Counter
import re

pypi_stopwords = get_stop_words('en')



def tokenizeNLTKSentence(dataset):
    
    new_dataset = list()
    for story in dataset:
        
        new_dataset.append(sent_tokenize(story))
        
    return new_dataset

def removePunctuation4(text):
    
    table = str.maketrans({key: None for key in string.punctuation})
    text = text.translate(table)
    return text

def removeNoiseSWR2(cleanText):
    
    stop_words_set = set(pypi_stopwords)
    #stop_words_set.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) # better do regex to cleanup.
    
    list_of_words = []
    list_of_words = list(set([word.lower() for word in cleanText.split()]) - set(stop_words_set))

    return list_of_words

def normaliseText(text):
    
    cleanText = removePunctuation4(text)
    cleanText = removeNoiseSWR2(cleanText)
    print(cleanText)
    return cleanText
    

text = """
            The present condition of the earth has been very challenging for the healthy existence of life because of the toxic environment, air pollution, water pollution, global warming, deforestation, and many more environmental issues. 
            There are numerous easy ways we can save our planet however, depends on the dedication and rate of good habit followers. It should be promoted the development of environment friendly technologies so that they could not harm the planet. 
            People should make the habit of reduction in usage of harmful things, re-usage and recycle of things in order to generate less amount of wastes.
            Generally, many people use variety of house cleansers in order to keep their houses clean and disinfected. They never see the chemical constituents of that particular cleanser which can be very destructive to the water, soil and air. 
            We should be very clear about what products we are using in daily life and always select eco-friendly cleansing products. Pollutions and global warming are generally being spread by the commercial industries to a great extent. 
            They should follow the government rules and regulations made for controlling the same.
            They should limit their harmful commercial-grade production and involve in producing environment friendly products. 
            Awareness regarding save earth should be promoted among youths by including this topic to their study. 
            They should be involved in the activities like planting, group discussion, essay writing, speech recitation, banner making, slogan writing competition, theme based drama play, etc in the school and college. 
            The event named as Earth Day is celebrated annually on 22nd of April to spread awareness regarding save earth among public.

      """
      

cleanText = normaliseText(text)

wordsDict = Counter((" ".join(str(word) for word in cleanText)).split())


sentences = sent_tokenize(text)
print(len(sentences)) # 13

cleansentences = []
for everysentence in sentences:
    cleansentences.append(removePunctuation4(everysentence.strip().lower()))
    

eachSentValue = {}
'''
{'awareness regar': 10,
 'generally many ': 12,
 'it should be pr': 7,
 'people should m': 14,
 'pollutions and ': 9,
 'the event named': 14,
 'the present con': 18,
 'there are numer': 13,
 'they never see ': 11,
 'they should be ': 21,
 'they should fol': 6,
 'they should lim': 9,
 'we should be ve': 9}
'''

for everysentence in cleansentences:

    for key, value in wordsDict.items():
        if key in everysentence.split():
            
            sentencehash = everysentence[:15]
            
            if sentencehash not in eachSentValue:
                eachSentValue[sentencehash] = value
            else:
                eachSentValue[sentencehash] += value
                

print(len(eachSentValue)) #13


sum = 0
for sentencehash in eachSentValue:
    sum += eachSentValue[sentencehash] #153

threshold = sum/len(eachSentValue) #11.76923076923077

summary = ''

for everysentence in cleansentences:
        
    if everysentence[:15] in eachSentValue and eachSentValue[everysentence[:15]] > (1.5 * threshold):
            summary +=  " " + everysentence

print(len(summary.split())) #63
"""
 'the present condition of the earth has been very challenging for the healthy existence of life because of
 the toxic environment air pollution water pollution global warming deforestation and many more environmental
 issues they should be involved in the activities like planting group discussion essay writing speech 
 recitation banner making slogan writing competition theme based drama play etc in the school and college'
"""


