[![Wisdomic Panda](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/panda.png)](http://www.rohanbagwe.com/)  **Wisdomic Panda**
> *Hold the Vision, Trust the Process.*

## Natural Language Processing: A Py Kick-off Digest! 
###### Natural Language Processing in Python.

# Named Entity Recognition
*... producing meaningful actionable insight from unstructured data.*

![NER](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/ner.jpeg)

**Named-entity recognition (NER)** (also known as entity identification, entity chunking and entity extraction) is a subtask of information extraction that seeks to locate and classify elements in text into pre-defined categories such as the names of persons, organizations, locations, expressions of times, quantities, monetary values, percentages, etc.



Word sense disambiguation: Some language words have multiple meanings according to their usage. For example, in the two sentences below:

		"Please book my flight for Delhi.”

		"I am going to read this book in the flight."

"Book" is used with different context, however the part of speech tag for both of the cases are different. In sentence I, the word " book"  is used as verb, while in next it is used as noun. 


Entities are defined as the most important chunks of a sentence – noun phrases, verb phrases or both. Entity Detection algorithms are generally ensemble models of rule based parsing, dictionary lookups, pos tagging and dependency parsing. The applicability of entity detection can be seen in the automated chat bots, content analyzers and consumer insights.



## Named Entity Recognition (NER)

> :pushpin: The process of detecting the named entities such as person names, location names, company names etc from the text is called as NER. 

**Example** 

	Sergey Brin, the manager of Google Inc. is walking in the streets of New York.

	Named Entities –  ( “person” : “Sergey Brin” ), (“org” : “Google Inc.”), (“location” : “New York”)

### A typical NER model consists of three blocks:

**Noun phrase identification**: This step deals with extracting all the noun phrases from a text using dependency parsing and part of speech tagging.

**Phrase classification**: This is the classification step in which all the extracted noun phrases are classified into respective categories (locations, names etc). Google Maps API provides a good path to disambiguate locations, Then, the open databases from dbpedia, wikipedia can be used to identify person names or company names. Apart from this, one can curate the lookup tables and dictionaries by combining information from different sources.

**Entity disambiguation**: Sometimes it is possible that entities are misclassified, hence creating a validation layer on top of the results is useful. Use of knowledge graphs can be exploited for this purposes. The popular knowledge graphs are – Google Knowledge Graph, IBM Watson and Wikipedia. 


:pushpin: [Personal Favourite: spaCy](https://spacy.io/api/annotation#named-entities)
