#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 11:43:48 2018

@author: Rohan

Building a corpus from Wikipedia dump file.
Download Data from: https://dumps.wikimedia.org/enwiki/latest/
"""

# pip intall gensim

from gensim.corpora import WikiCorpus
import time

start_time = time.time()

# Creates an Empty file to dump data.
 
target = open('Wiki_Data.txt', 'w')
wiki_data = WikiCorpus('enwiki-latest-pages-articles15.xml-p7744803p9244803.bz2')

i = 0
for text in wiki_data.get_texts():
    target.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
    i = i + 1
    if (i % 10000 == 0):
        print('Extracted ' + str(i) + ' articles')
target.close()

print(" Data Extraction Completed in %d seconds!" %(time.time() - start_time))

"""
Extracted 10000 articles
Extracted 20000 articles
Extracted 30000 articles
Extracted 40000 articles
Extracted 50000 articles
Extracted 60000 articles
Extracted 70000 articles
Extracted 80000 articles
Extracted 90000 articles
Extracted 100000 articles
Extracted 110000 articles
Extracted 120000 articles
 Data Extraction Completed in 1623 seconds!

"""
