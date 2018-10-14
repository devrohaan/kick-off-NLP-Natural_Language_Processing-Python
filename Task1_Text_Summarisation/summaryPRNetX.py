#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 20:05:02 2018

@author: Rohan
"""
import nltk
from nltk import sent_tokenize
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
import string
import networkx


import matplotlib
import numpy as np

%matplotlib inline


def removePunctuation4(text):
    
    table = str.maketrans({key: None for key in string.punctuation})
    text = text.translate(table)
    return text



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
      

a=set([word for word in "ROhan is the zhatu".split() if word not in stop_words])
       
sentences = sent_tokenize(text)
cleansentences = []
for everysentence in sentences:
    cleansentences.append(list(set([word for word in removePunctuation4(everysentence.strip().lower()).split() if word not in stop_words])))

graphSent = []
for everysentence in sentences:
    graphSent.append(removePunctuation4(everysentence.strip().lower()))

graph = networkx.Graph()





setenceDict = {}
for index,everysentence in enumerate(graphSent):
    sentenceHash = everysentence[:15]
    setenceDict[index] = sentenceHash

{0: 'the present con',
 1: 'there are numer',
 2: 'it should be pr',
 3: 'people should m',
 4: 'generally many ',
 5: 'they never see ',
 6: 'we should be ve',
 7: 'pollutions and ',
 8: 'they should fol',
 9: 'they should lim',
 10: 'awareness regar',
 11: 'they should be ',
 12: 'the event named'}


graph.add_nodes_from(setenceDict.keys())


# Here, bigrams are "tagged bigrams".
bigrams = nltk.ngrams(tagged_tokens, 2)


matplotlib.rcParams['figure.figsize'] = (10.0, 12.0)
networkx.draw_networkx(graph)



def addEdge(graphSent,graph):
    
    transitionProbMatrix = np.zeros((len(graphSent), len(graphSent)))
    
    for indexOuter, everysentence in enumerate(graphSent):
        
        for indexInner, everysentenceInner in enumerate(graphSent):
            
            wordcount = 0
            if everysentence[:15] == everysentenceInner[:15]: #skip compariosn with same sentence
                print("same")
                continue
            else:
                
                for word in list(set(everysentence.split())-set(stop_words)):
                    if word in everysentenceInner:
                        wordcount+=1
                
                prob = (wordcount/(len(everysentence)+len(everysentenceInner)))*100
                print(prob)
                if prob > 0.4:
                    graph.add_edge(indexOuter, indexInner)            
                
    
    return graph

graph = addEdge(graphSent,graph)

pagerank = networkx.pagerank(graph)
# Then sort the nodes according to the rank.# Then s 
ranked = sorted(pagerank.items(), key=lambda ns_pair: ns_pair[1], reverse=True)
# We only keep 20% of the top-ranking nodes.
selectivity = 0.20
remove_n = int(len(ranked) * selectivity)



# Now remove the nodes we don't need.# Now re 
for node, _ in ranked[remove_n:]:
    graph.remove_node(node)
    

# Let's see how many are left.# Let's  
len(graph)

networkx.draw_networkx(graph)

summaryList = list(graph) #[1,4]

print('. '.join(graphSent[index] for index in summaryList))

"""
there are numerous easy ways we can save our planet however depends on the dedication and rate of good habit followers. generally many people use variety of house cleansers in order to keep their houses clean and disinfected
"""

