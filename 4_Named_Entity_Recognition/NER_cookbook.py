#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 12:32:22 2018

@author: Rohan
"""
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
sentence="Sara sells seashells on the seashore"
tokenized = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokenized)
print(tagged)

"""
[('Sara', 'NNP'), ('sells', 'VBZ'), ('seashells', 'NNS'), ('on', 'IN'), ('the', 'DT'), ('seashore', 'NN')]

"""

namedEnt = nltk.ne_chunk(tagged)
namedEnt.draw()

from nltk.tag import StanfordNERTagger

model = '/Users/Rohan/Desktop/3rdAug/NLP/4_Named_Entity_Recognition/stanfordner/classifiers/english.all.3class.distsim.crf.ser.gz'
jar = '/Users/Rohan/Desktop/3rdAug/NLP/4_Named_Entity_Recognition/stanfordner/stanford-ner.jar'
st = StanfordNERTagger(model, jar) 
st.tag('Sara sells seashells on the seashore'.split()) 

"""
[('Sara', 'PERSON'),
 ('sells', 'O'),
 ('seashells', 'O'),
 ('on', 'O'),
 ('the', 'O'),
 ('seashore', 'O')]
"""

import spacy
"""
For OS X
 export LC_ALL=en_US.UTF-8
 export LANG=en_US.UTF-8
 
python -m spacy download en
python -m spacy download en_core_web_sm
"""

nlp=spacy.load('en_core_web_sm')
sentence="Ram of Apple Inc. travelled to Sydney on 5th October 2017"
for token in nlp(sentence):
   print(token, token.ent_type_)



sentence="Apple India Sydney Rohan Banana"
for token in nlp(sentence):
   print(token, token.ent_type_)
   
st.tag(sentence.split())    
   
   
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
  
"""
Apple 0 5 ORG
U.K. 27 31 GPE
$1 billion 44 54 MONEY
"""

from spacy import displacy

nlp = spacy.load('en')
doc = nlp(u'This is a sentence.')
displacy.serve(doc, style='dep')

