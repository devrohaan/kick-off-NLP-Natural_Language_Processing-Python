[![Wisdomic Panda](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/panda.png)](http://www.rohanbagwe.com/)  **Wisdomic Panda**
> *Hold the Vision, Trust the Process.*


## Natural Language Processing: A Py Kick-off Digest!
###### Natural Language Processing in Python.

# Text Classification
*... assigning categories to documents.*


**Text classification**, in common words is defined as a technique to systematically classify a text (document or sentence) in one of the fixed category. It is really helpful when the amount of data is too large, especially for organizing, information filtering, and storage purposes.

![TC](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/tc.png)

Text classification is one of the classical problem of NLP.  

**Examples:**

- Email Spam Identification.
- Topic classification of news.
- sentiment classification.
-  Organization of web pages by search engines.



## Text classification algorithm:

### The “Bag of Words” (or BoW) Approach.


:bulb: It requires compiling a list of "keywords" (words from a document) that qualifies the type of content in document to a certain topic.

:bulb: If one or more qualifying keywords are present in a document then the document is assigned to the topic. 

**Example**

**Doc1**: Cristaino Ronaldo started **playing** **football* at a very young age. [Sport]

**Doc2**: Modrić is one of the most influential **football** **players**. [Sport]

**Doc3**: My favourite **movie** is Avatar which premiered in 2009. [Entertainment] 

Machine learning algorithms cannot work with raw text directly; the text must be converted into numbers. Specifically, vectors of numbers.


So, before the classification, we need to transform the words (or tokens) from dataset to more compress and understandable information for the model. This process is called featurization or feature extraction.

> :pushpin: Feature extraction is the process of transforming the input data into a set of features which can very well represent the input data.

A popular and simple method of feature extraction with text data is called the bag-of-words model of text.


BoW is a simple but effective method for feature extraction.


> Segment each text file into words.
> Count number of times each word occurs in each document.
> Assign each word an integer id. 
> **Each unique word in our dictionary will correspond to a feature.(descriptive feature)**

**Example**

    Doc1: Ronaldo playes Forward
    Doc2: Mordirć  playes Midfielder

    Doc1 = ['Ronaldo', 'playes', 'Forward']
    Doc2 = [Mordirć, 'playes', 'Midfielder']

    The vocabulary will be:
    
    bow = {'Ronaldo':0,'playes':1,'Mordirć':2,'Midfielder':3,'Forward':4}

    and the features for each documents are:
 
    f1 = [1, 1, 0, 0, 1]
    f2 = [0, 1, 1, 1, 0]


### On a similar note.

Feature Label vector will be created as below for above documents.

    feature_bow = {"other":0,"sports":1}
    f_label = [1,1]


In the worked example, we have already seen one very simple approach to scoring: a binary scoring of the presence or absence of words.

Some additional simple scoring methods include:

**Counts**: Count the number of times each word appears in a document.
**Frequencies**: Calculate the frequency that each word appears in a document out of all the words in the document.


The code for building a Bow model is shown as: [BOW]()

> :pushpin: A more sophisticated approach is to create a vocabulary of grouped words. This both changes the scope of the vocabulary and allows the bag-of-words to capture a little bit more meaning from the document.

> In this approach, each word or token is called a "gram". Creating a vocabulary of two-word pairs is, in turn, called a bigram model. 

> :pushpin: A vocabulary then tracks triplets of words is called a trigram model and the general approach is called the n-gram model, where n refers to the number of grouped words.





## A NL Text classifier consists of two parts: 

-  Feature Extraction, BOW.
-  Training 
-  Prediction 

**Firstly, the text input is processed and features are created, as we have seen above using BOW approach.**

We divide the batch of features along with the created labels into a train and test set.

**The machine learning models then learn these features and is used for predicting against the new text.**

> :pushpin: I will train some basic models with Scikit learn as it is one of the standard tools for text processing, NLP, and Machine learning. It eases the development of NLP applications and has a plethora of Machine Learning models and tools. 

The code for building a Text Classfifcation model: [kick-NBC]()


:scroll: [Paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.95.9153&rep=rep1&type=pdf)
