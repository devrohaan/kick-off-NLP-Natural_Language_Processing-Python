[![Wisdomic Panda](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/panda.png)](http://www.rohanbagwe.com/)  **Wisdomic Panda**
> *Hold the Vision, Trust the Process.*

## Natural Language Processing: A Py Kick-off Digest! 
###### Natural Language Processing in Python.

# Data Normalization
*... unifying the multiple representations exhibited by single word.*

![Normalise](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/normal.png)

## Pre-Processing Normalization:

*"Normalization consists of the translation (mapping) of terms in the scheme or linguistic reductions through Stemming, Lemmazation and other forms of standardization."*

It consists of a number of steps, any number of which may or not apply to a given task, but generally fall under the broad categories of tokenization, normalization, and substitution.

> :pushpin: When we preprocess the data, in NLP we name it text normalization or data preparation.


To cite an example – **“play”**, **“player”**, **“played”**, **“plays”** and **“playing”** are the different variations of the word – **“play”**, Though they mean different but contextually all are similar. The step converts all these forms of a word into their normalized form (also known as lemma). Normalization is a pivotal step for feature engineering with text as it converts the high dimensional features (N different features) to the low dimensional space (1 feature), which is an ideal ask for any ML model.


## The most common normalization practices are :

- **Tokenization:** Tokenization describes splitting paragraphs into sentences, or sentences into individual words. For the former Sentence Boundary Disambiguation (SBD) can be applied to create a list of individual sentences. This relies on a pre-trained, language specific algorithms like the Punkt Models from NLTK.

Sentences can be split into individual words and punctuation through a similar process. Most commonly this split across white spaces, for example:

      IN:
      "Hold the vision, trust the process."
      OUT:
      ['Hold','the','vision',',','trust','the','process','.']
      

- **Stemming:**  Stemming is a rudimentary rule-based process of eliminating (suffixed, prefixes, infixes, circumfixes) from a word in order to obtain a word stem. (“ing”, “ly”, “es”, “s” etc.)

      
There are occasions that this can cause problems when a word is abbreviated, truncated or is possessive. Proper nouns may also suffer in the case of names that use punctuation (like O’Neil).





- **Lemmatization:** Lemmatization, on the other hand, is an organized & step by step procedure of obtaining the root form of the word, it makes use of vocabulary (dictionary importance of words) and morphological analysis (word structure and grammar relations). Lemmazation is an alternative approach from stemming to removing inflection and can get better results.


> :pushpin: Stemming works on words without knowing their context, which is why it has lower accuracy and is faster than lemmatization. Lemmazation is a more intensive and therefor slower process, but more accurate. Stemming may be more useful in queries for databases whereas lemmazation may work much better when trying to determine text sentiment. stemming the word "better" would fail to return its citation form, but lemmatization would result in the following: better → good

> :pushpin: In my opinion, lemmatizing is better than stemming. Word lemmatizing returns a real word even if it's not the same word; it could be a synonym, but at least it's a real word. Sometimes, you don't care about this level of accuracy, and all you need is speed. In this case, stemming is better.


- **Capitalization:** Text often has a variety of capitalization reflecting the beginning of sentences, proper nouns emphasis. The most common approach is to reduce everything to lower case for simplicity but it is important to remember that some words, like “US” to “us”, can change meanings when reduced to the lower case.

- **Stopword:** A majority of the words in a given text are connecting parts of a sentence rather than showing subjects, objects or intent. Word like “the” or “and” cab be removed by comparing text to a list of stopword.

      IN:
      There are two great days in a person's life - the day we are born and the day we discover why.
      
      Tokenization:
      ['There', 'are', 'two', 'great', 'days', 'in', 'a', 'person's', 'life', '-', 'the', 'day', 'we', 'are', 'born', 'and', 'the', 'day', 'we', 'discover', 'why']
      
      OUT:
      [ 'two', 'days', 'person's', 'life', 'day', 'born', 'day', 'discover', 'why']

> :pushpin:  In the example above it reduced the list of 20 words to 9, but it is important to note that the word “and” was dropped which separated the two reasons. One might create their own stopword dictionary manually or utilize prebuilt libraries depending on the sensitivity required.

Normalizations are major parts of a text preprocessing! 
There are, however, numerous other steps which we learrned in previous write-up that can be taken to help put all text on equal grounds.


-	set all characters to lowercase.
-	remove numbers (or convert numbers to textual representations).
-	remove punctuation (generally part of tokenization, but still worth keeping in mind at this stage, even as confirmation).
-	strip white space (also generally part of tokenization).
-	remove default stop words (general English stop words).

### 2. Cookbooks
**- [Cookbook](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/blob/master/2_Data_Preprocessing_Normalization/Data_Preprocessing_Example.ipynb)**

**- [Data Cleaning Utility](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/blob/master/2_Data_Preprocessing_Normalization/functions_cookbook.py)**

## :bulb: Trade-off: Normalization vs. Information


> :pushpin: This means that depending on the task we would want all the words to be lowercased or to convert plural terms into singular ones if we don’t want to consider dog and dogs as two different entities.
We might encounter different forms of the same verb in a document and we would want to consider just that verb instead of making a distinction between each form.
when we normalize we are losing part of the information in exchange of being able to generalize better.
This normalization/information trade-off is common in the study of data, but also very important in the study of natural language.
