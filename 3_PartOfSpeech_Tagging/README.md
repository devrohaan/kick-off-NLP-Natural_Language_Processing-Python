[![Wisdomic Panda](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/panda.png)](http://www.rohanbagwe.com/)  **Wisdomic Panda**
> *Hold the Vision, Trust the Process.*


## Natural Language Processing: A Py Kick-off Digest! 
###### Natural Language Processing in Python.

# Part of Speech Tagging
*... the grammatical function of the words in the corpus*


![POSS](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/poss.png)


Syntax and structure of a natural language such as English are tied with a set of specific rules, conventions, and principles which dictate how words are combined into phrases, phrases get combined into clauses, and clauses get combined into sentences. All these constituents exist together in any sentence and are related to each other in a hierarchical structure.

**Example** 

###### Subject and Predicate relationship. 

		Ronaldo is playing football.

This sentence is talking about two subjects - **Ronaldo** and **football**. 

> To find the subject of the sentence, it is easier to first find the verb and then find "who" or "what" around it. 

In the above sentence, "playing" is the verb of predicate. If you ask "Who is playing?", the answer is "Ronaldo" which gives the first subject, and "What is he playing?" gives us "football" as the other subject. An extensive combination of similar rules allows us to define the entities (subjects), intent (predicates), the relationship between intent and entity, etc.

Such an analysis is very useful in any NLP application since it defines some meaning of the text. In a collection of words without any relation or structure, it is very difficult to ascertain what it might be trying to convey or what it means.


> :pushpin: Part-Of-Speech Tagging is the process of marking up of words in a sentence as nouns, verbs, adjectives, adverbs etc.


### POS tags and their notations

> :pushpin: In English language there are broadly 8 parts of speech: nouns, adjectives, pronouns, interjections, conjunctions, prepositions, adverbs, verbs. In Penn Treebank, a commonly used dataset for language syntax and structure, there are 47 tags defined which are widely used in text analytics and NLP applications. 
> - Noun (N)- Ronaldo, Manchester, table, dog, teacher, pen, city, happiness, hope
> - Verb (V)- go, speak, run, eat, play, live, walk, have, like, are, is
> - Adjective(ADJ)- big, happy, green, young, fun, crazy, three
> - Adverb(ADV)- slowly, quietly, very, always, never, too, well, tomorrow
> - Preposition (P)- at, on, in, from, with, near, between, about, under
> - Conjunction (CON)- and, or, but, because, so, yet, unless, since, if
> - Pronoun(PRO)- I, you, we, they, he, she, it, me, us, them, him, her, this
> - Interjection (INT)- Ouch! Wow! Great! Help! Oh! Hey! Hi!


[Here is a list of all possible pos-tags defined by Pennsylvania university.](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/PennTaggset.pdf)


## POS taggers

###### Approaches used to build a POS taggers:

- Rule based
- Statistics based
- Supervised learning based

*... stay tuned for more details coming soon.*


## Chunking

Chunking is a process of extracting phrases from unstructured text. Instead of just simple tokens which may not represent the actual meaning of the text, its advisable to use phrases such as **"Cristiano Ronaldo"** as a single word instead of **'Cristiano'** and **'Ronaldo'** separate words.

Chunking works on top of POS tagging, it uses pos-tags as input and provides chunks as output. Similar to POS tags, there are a standard set of Chunk tags like Noun Phrase(NP), Verb Phrase (VP), etc. 

> :pushpin: Chunking is very important when you want to extract information from text such as Locations, Person Names etc. In NLP called Named Entity Extraction.

There are a lot of libraries which gives phrases out-of-box such as Spacy or TextBlob.




## Applications

Some applications of POS tagging is to narrow down the nouns to focus on most prominent ones, or to perform qualifier-subject analysis, word sense disambiguation, grammar analysis, etc. The most important use case is to extract phrases from the sentence.

![POS Tagset](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/POS.png)


:bulb: [Advanced Learning](http://language.worldofcomputing.net/pos-tagging/parts-of-speech-tagging.html)
