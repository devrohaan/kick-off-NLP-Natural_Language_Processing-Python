[![Wisdomic Panda](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/panda.png)](http://www.rohanbagwe.com/)  **Wisdomic Panda**
> *Hold the Vision, Trust the Process.*


## Natural Language Processing: A Py Kick-off Digest! 
###### Natural Language Processing in Python.

# Data Cleaning
*... producing meaningful actionable insight from unstructured data.*

![Clean](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/cleaner.gif)

One of the first steps in working with text data is to pre-process it. It is an essential step before the data is ready for analysis. Majority of available text data is highly unstructured and noisy in nature – to achieve better insights or to build better algorithms, it is necessary to play with clean data. For example, social media data is highly unstructured – it is an informal communication – typos, bad grammar, usage of slang, presence of unwanted content like URLs, Stopwords, Expressions etc. are the usual suspects.

> :pushpin: Today, more than 80% of the data is unstructured – it is either present in data silos or scattered around the digital archives. Data is being produced as we speak – from every conversation we make in the social media to every content generated from news sources.


## we can refer to two main types of data:

> **Structured data:** information that has a pre-defined structure, which is typically represented in a numerical way but can also include text. A good example is an SQL table.


> **Unstructured data:** This is a large chunk of the total amount of data that we consume and produce every day.
Information that does not have a well defined systematic structure. When we deal with natural language, we are dealing with unstructured data. we can’t specify a universal structure that a sentence can have.


We can conceive NLP as the different set of tools that can be applied in order to structure natural language for different purposes.
We can think of this corpus as the set of Lego© pieces. When we remove the damaged or unuseful pieces from lego from our set, this is called the preprocessing step in which we try to select useful pieces for the building process.

Text data often contains words or phrases which are not present in any standard lexical dictionaries. 
Acronyms, hashtags with attached words, and colloquial slangs. With the help of regular expressions and manually prepared data dictionaries, this type of noise can be fixed


### In a nutshell,

Data preprocessing consist of getting rid of the less useful parts of text through stopword removal, dealing with capitalization and characters and other details.


###### Lets analyze this tweet when Sir Alex Ferguson has undergone surgery for a brain haemorrhage.

     Get well soon fergy lad lt;3!!! u're a awsm legend. As a Man City fan ... I wish Sir Alex a speedy recovery &amp
     send my best wishes to his family at this difficult time. #ManchesterCityFan#footballfan 💙💙 

## Data Pre-Processing: Cleaning

#### Text can come in a variety of forms from a list of individual words, to sentences to multiple paragraphs with special characters (like tweets for example) and transforming the text into something an algorithm can digest it a complicated process. Like any data science problem, understand the questions that are being asked will inform what steps may be employed to transform words into numerical features that work with machine learning algorithms.


### Removing Noise

Let's assume we obtained a corpus from the world wide web, and that it is housed in a raw web format. We can, then, assume that there is a high chance our text could be wrapped in HTML or XML tags.


- remove text file headers, footers.
- remove HTML, XML, etc. markup and metadata.
- extract valuable data from other formats, such as JSON, or from within databases.
- regex should be your best friend.


> :pushpin: There are a variety of pre-processing methods. This [cookbook]() is far from exclusive list but it does give an idea of where to start. It concentrates on possible noise elements and how you could clean them step by step. 
It is important to realize, like with all data problems, converting anything into a format for machine learning reduces it to a generalized state which means losing some of the fidelity of the data along the way. I have devised few tricks while working with a lot of textual data. If you follow the above steps to clean the data, you can drastically improve the accuracy of your results and draw better insights. The true art is understand the pros and cons to each to carefully chose the right methods.

 *"There is no universal answer. It all depends on what you plan to use the vectors for. In my experience, it is usually good to disconnect (or remove) punctuation from words, and sometimes also convert all characters to lowercase. One can also replace all numbers (possibly greater than some constant) with some single token such as '.'*

*All these pre-processing steps aim to reduce the vocabulary size without removing any important content (which in some cases may not be true when you lowercase certain words, ie. ‘Bush’ is different than ‘bush’, while ‘Another’ has usually the same sense as ‘another’). The smaller the vocabulary is, the lower is the memory complexity, and the more robustly are the parameters for the words estimated. You also have to pre-process the test data in the same way." - Jason Brownlee*




> I would recommend practising these methods by applying them in machine learning/deep learning tasks.




