[![Wisdomic Panda](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/panda.png)](http://www.rohanbagwe.com/)  **Wisdomic Panda**
> *Hold the Vision, Trust the Process.*


## Natural Language Processing: A Py Kick-off Digest!
###### Natural Language Processing in Python.

# Word Embedding or Text Vectors
*... the modern way of representing words as vectors.*

![AI](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/embed.gif)

## Word Embedding: An Artificial Numerical World

We understand any natural language because of our shared experiences of the world we live in. For example, when your mom says ‘food’, we can associate symbols, imagine images and characteristics based on our previous real world experiences with ‘food’. 

Machines do not understand natural language. However, machines lonly understand numbers, not words. They communicate through ones and zeros and it is so different on how we communicate with one another through letters, words and symbols. The CPU of the computer reads binary machine instructions and executes them on binary data with RAM. They produce new electric signals on behalf of other electric signals. That’s it, that’s all it does.

So, in order for machines to really understand us, machines need to understand our world too. 


## What are Word Embeddings?

Word embedding is the modern way of representing words as vectors.
In very simplistic terms, Word Embeddings are the texts converted into numbers.
They are used to represent Natural Language in vector form of real numbers. They are useful because of computers’ inability to process Natural Language. So these Word Embeddings capture the essence and relationship between words in a Natural Language using real numbers.

A Word Embedding format generally tries to map a word using a dictionary to a vector and there may be different numerical representations (or vectors) of the same text.

The aim of word embedding is to redefine the high dimensional word features into low dimensional feature vectors. In other words it represents words at an X and Y vector coordinate where related words, based on a corpus of relationships, are placed closer together. Word2Vec and GloVe are the most common models to convert text to vectors.

A system developed by Google called Word2Vec has a math like function with words that works to fairly good success. 
                
       For example:
                   king - man + woman = queen

Well, a king can be considered a male in a seat of power. What do we call the female in the seat of power? Word2Vec will tell you the answer is 'queen', and in my opinion that’s a pretty good answer.


They are widely used in deep learning models such as Convolutional Neural Networks and Recurrent Neural Networks.


> :pushpin: A computer can match two strings and tell you whether they are same or not. But how do we make computers tell you about football or Real Madrid when you search for Ronaldo? How do you make a computer understand that 'An apple a day keeps the doctor away.' in this 'Apple' is a healthy fruit that can keep the doctor away and not the Apple company!!:grin:

> The answer to the above questions lie in creating a representation for words that capture their meanings, semantic relationships and the different types of contexts they are used in.
And all of these are implemented by using Word Embeddings or numerical representations of texts so that computers may handle them.



## Simplest Word Embedding

        data = "An apple a day keeps the doctor away"

        #Dictionary as a list of all unique words in the data.
        
        dict = ['An', 'apple', 'a', 'day', 'keeps', 'the', 'doctor', 'away']

        #The vector representation of "apple" in this format according to the above dictionary is:

        apple_Vec = [0,1,0,0,0,0,0,0]

        """A vector representation of a word may be a one-hot encoded 
        vector where 1 stands for the position where the word 
        exists and 0 everywhere else. """


## Different types of Word Embeddings

The different types of word embeddings can be broadly classified into two categories -

- 1. Frequency based Embedding
- 2. Prediction based Embedding

## 1. Frequency based Embedding

##### 1.1 Count Word Frequency

Unique words (or tokens are extracted out of the data (or corpus). These N tokens will form our dictionary and the size of the Count Vector matrix M will be given by D X N, where D is the number of Documents

###### Example

D1: the France: France Crowned World Cup 2018 Champions After Beating Croatia.

D2: France was clearly the best team in 2018 Word Cup.

        The dictionary created may be a list of unique tokens(or words) in the given corpus,
        Dict = ['France', 'Crowned' , 'Champions', 'clearly', 'was', 'World', 'Cup', '2018', 'Croatia', 'Beating', 'after', 'the','best', 'team', 'in']

Here, D=2, N=15

The count matrix M of size 2 X 15 will be represented as –

|   |France | was |clearly |Crowned |World |the| Cup| best|2018 |Champions |After| Beating| Croatia| team |in |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|D1| 2|0|0|1|1|1|1|0|1|1|1|1|1|0|0|
|D2| 1|1|1|0|1|1|1|0|1|0|0|0|0|1|1|

###### The word vector for **'France'** in the above matrix is **[2,1]** and so on. Here, the rows correspond to the documents in the corpus and the columns correspond to the tokens in the dictionary. 

### Bag of Words model

> Segment each text file into words
> Count number of times each word occurs in each document 
> Assign each word an integer id. 
> **Each unique word in our dictionary will correspond to a feature (descriptive feature)**

> :pushpin: Creating [Bag of Words]() model


> :pushpin: We might have a corpus which contains millions of documents. And with millions of document, we can extract hundreds of millions of unique words. So basically, the matrix that will be prepared like above will be a very sparse one and inefficient for any computation. So an alternative to using every unique word as a dictionary element would be to pick say top 10,000 words based on frequency and then prepare a dictionary.


###### 1.2 Term Frequency – Inverse Document Frequency


TF-IDF method which is based on the frequency method but it is different to the count vectorization in the sense that it takes into account not just the occurrence of a word in a single document but in the entire corpus.



Common words like ‘is’, ‘the’, ‘a’ etc. tend to appear quite frequently in comparison to the words which are important to a document. For example, a Doc1 on Ronaldo is going to contain more occurences of the word "Ronaldo" in comparison to other documents. But common words like "a","the" etc. are also going to be present in higher frequency in almost every document.

Ideally, what we would want is to down weight the common words occurring in almost all documents and give more importance to words that appear in a subset of documents.

TF-IDF works by penalising these common words by assigning them lower weights while giving importance to words like Ronaldo in a particular document.


Consider the below sample Docs:

###### Doc1

|Tokens|Count|
|:---:|:---:|
|CR7|6|
|**Ronaldo**|70|
|he|39|
|is|70|
|goals|4|


###### Doc2

|Tokens|Count|
|:---:|:---:|
|this|2|
|match|1|
|he|30|
|is|33|
|goals|6|

TF = (Number of times term t appears in a document)/(Number of terms in the document)

            TF(goals,Doc1) = 4/139

            TF(goals, Doc2) = 6/72

It denotes the contribution of the word to the document i.e words relevant to the document should be frequent. eg: A document about Ronaldo should contain the word Ronaldo in large number.

IDF = log(N/n), where, N is the number of documents and n is the number of documents a term t has appeared in.

where N is the number of documents and n is the number of documents a term t has appeared in.

        So, IDF(goals) = log(2/2) = 0.

### :bulb: Idea: If a word has appeared in all the document, then probably that word is not relevant to a particular document. But if it has appeared in a subset of documents then probably the word is of some relevance to the documents it is present in.

Let us compute IDF for the word 'Ronaldo'.

        IDF(Ronaldo) = log(2/1) = 0.301.

Now, let us compare the TF-IDF for a common word ‘he’ and a word ‘Ronaldo’ which seems to be of relevance to Doc1.

        TF-IDF(goals,Doc1) = (4/139) * (0) = 0

        TF-IDF(he, Doc2) = (30/72) * (0) = 0

        TF-IDF(Ronaldo, Doc1) = (70/139)*0.301 = 0.152

As, you can see for Doc1 , TF-IDF method heavily penalises the words goals, he, is but assigns greater weight to Ronaldo. So, this may be understood as Ronaldo is an important word for Document1 from the context of the entire corpus.

### Example: [TF-IDF](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/blob/master/5_Word_Embeddings/TF_IDF_RonaldoDoc_EarthDoc.ipynb)

###### 1.3 Co-Occurrence Matrix with a fixed context window

Words co-occurrence matrix describes how words occur together that in turn captures the relationships between words. 

> :pushpin: Similar words tend to occur together and will have similar context.

Words co-occurrence matrix is computed simply by counting how two or more words occur together in a given corpus.

**Example** – Ronaldo is a footballer. Modric is a footballer.
Ronaldo and Modric tend to have a similar context i.e footballer.


**Co-occurrence** – For a given corpus, the co-occurrence of a pair of words say "w1" and "w2" is the **number of times they have appeared together in a Context Window.**

**Context Window** – Context window is specified by a number of words taken an as a frame and the direction.

Now, let us take an example corpus to calculate a co-occurrence matrix.

Corpus = a friend in need is a friend indeed
         you are the best friend indeed

We can summarize co-occurrence statistics for words 'a' and 'friend' as:

||a|friend|in|need|is|indeed|you|are|the|best|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**a**|0|:hatched_chick:2|0|0|0|0|0|0|0|0|
|**friend**|:hatched_chick:2|0|1|0|0|:hatched_chick:2|0|0|0|:hatched_chick:1|

The above table shows that '**a**'' is followed twice by '**friend**' while words **indeed** and **best** appear once around '**friend**' in our corpus. Thus, **indeed** is one out of two times probable to appear after '**friend**'.

 The count shown above is called bigram frequency; it looks into only the next word from a current word. 
###### [NgramGenerate](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/blob/master/5_Word_Embeddings/NgramGenerate.py)

 Given a corpus of N words, we need a table of size NxN to represent bigram frequencies of all possible word-pairs. Such a table is highly sparse as most frequencies are equal to zero. ### In practice, the co-occurrence counts are converted to probabilities.

> :pushpin: Co-occurrence matrix is not the word vector representation that is generally used. Instead, this Co-occurrence matrix is decomposed using techniques like PCA (Principal component analysis) etc. into factors and combination of these factors forms the word vector representation. 

> For example, you perform PCA on the above matrix of size NXN. You will obtain V principal components. You can choose k components out of these V components. So, the new matrix will be of the form N X k.
And, a single word, instead of being represented in N dimensions will be represented in k dimensions while still capturing almost the same semantic meaning. k is generally of the order of hundreds.



#### 2 Prediction based Vector

###### Pre-requisite: Knowledge of how a neural network works and the mechanisms by which weights in an NN are updated. Kindly go throgh [The_First_Artificial_Neural_Network](https://github.com/robagwe/kick-off-Oracle_of_Football-The_First_Artificial_Neural_Network) for better understanding of ANN working.
 

Tomas Mikolov at Google introduced word2vec algorithm to the world. Embedding vectors created using the Word2vec algorithm have many advantages compared to earlier algorithms. This algorithm was prediction based in the sense that they provided probabilities to the words and proved to be state of the art for tasks like word analogies and word similarities.


> *"The idea behind Word2Vec is pretty simple. We’re making an assumption that the meaning of a word can be inferred by the company it keeps. This is analogous to the saying, “show me your friends, and I’ll tell who you are”. If you have two words that have very similar neighbors (meaning: the context in which its used is about the same), then these words are probably quite similar in meaning or are at least related. For example, the words shocked, appalled and astonished are usually used in a similar context." - John Firth, Kavita Ganesan*

### Word2vec is not a single algorithm but a combination of two techniques – CBOW (Continuous bag of words) and Skip-gram model. 

![w2v](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/w2v.png)

###### 2.1 CBOW (Continuous bag of words)

CBOW tends to predict the probability of a word given a context. A context may be a single word or a group of words. 

CBOW uses the context or surrounding words as input. For instance, if the context window C is set to C=5, then the input would be words at positions w(t-2), w(t-1), w(t+1), and w(t+2). Basically the two words before and after the center word w(t). Given this information, CBOW then tries to predict the target word.

![onehot](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/1hot.png)


###### 2.2 Skip-gram model

Another approach is to create a model such that given the center word “jumped”, the model will be able to predict or generate the surrounding words “The”, “cat”, “over”, “the”, “puddle”. Here we call the word “jumped” the context. We call this type of model a SkipGram model.

Skip-gram model reverses the use of target and context words. Skip-gram take a word and predict the context word from it.

Instead of inputting the context words and predicting the center word, we feed in the center word and predict the context words. This means that w(t) becomes the input while w(t-2), w(t-1), w(t+1), and w(t+2) are the ideal output.

Now we need to feed this data into a NN train it.


> :pushpin: Though CBOW (predict target from context) and skip-gram (predict context words from target) are just inverted methods to each other, they each have their advantages/disadvantage. Since CBOW can use many context words to predict the 1 target word, it can essentially smooth out over the distribution. This is essentially like regularization and is offer very good performance when our input data is not so large. However the skip-gram model is more fine grained so we are able to extract more information and essentially have more accurate embeddings when we have a large data set (large data is always the best regularizer). Skip-gram with negative sub-sampling outperforms every other method generally.


> :bulb: Word2vec is an algorithm invented at Google for training word embeddings. Word2vec relies on the distributional hypothesis to map semantically similar words to geometrically close embedding vectors.
The distributional hypothesis states that words which often have the same neighboring words tend to be semantically similar. Both "dog" and "cat" frequently appear close to the word "vet", and this fact reflects their semantic similarity.


# [CBOW](https://github.com/thushv89/udacity_deeplearning_complete/blob/master/5_word2vec_CBOW.ipynb) Vs [Skip-gram](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/5_word2vec.ipynb)

## Word2Vec Implementations, pre-trained model & Papers.

:pencil2: [Word2Vec PyTf](http://adventuresinmachinelearning.com/word2vec-tutorial-tensorflow/)

:mag: [Chris McCormick: The Skip-Gram](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/)

:mag: [Word2Vec for NLP](https://www.kaggle.com/c/word2vec-nlp-tutorial#description)

#### Pre-trained Word Vectors
:minidisc: [Tiny GloVe pre-trained model](http://nlp.stanford.edu/data/glove.6B.zip)

:minidisc: [GloVe Docs](https://nlp.stanford.edu/projects/glove/)

:minidisc: [Google Pre-trained word2vec](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing)

###### Here is an exhaustive list of pre-trained Word Vectors in 294 languages by facebook.
:minidisc: [Facebook Pre-trained](https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md)

:minidisc: [Kyubyong](https://github.com/Kyubyong/wordvectors)

:minidisc: [Kyubyong](https://github.com/Kyubyong/wordvectors)

:scroll: [Paper](https://arxiv.org/pdf/1411.2738.pdf)

:scroll: [Tomas Mikolov Paper](https://arxiv.org/abs/1301.3781)
## Applications

- Text Vectors can be used as feature vectors for ML model, used to measure text similarity using cosine similarity techniques, words clustering and text classification techniques.

![pun](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/pun.jpeg)

