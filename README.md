[![Wisdomic Panda](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/panda.png)](http://www.rohanbagwe.com/)  **Wisdomic Panda**
> *Hold the Vision, Trust the Process.*

# Natural Language Processing: A Py Kick-off Digest! 
"*A computer could be considered intelligent if it could carry on a conversation with a human being without the human realizing they were talking to a machine. -Alan Turing*"
###### Natural Language Processing in Python.

**Why?**

![Rosie](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/1.gif)

My belief in machine intelligence grew stronger as I became acquainted with artificial personalities like Eliza and Alice that were capable of processing natural language. Today we see how Deep Learning, a branch of Machine Learning techniques, has obtained a high performance in generating rational conclusions in Natural Language Processing (or NLP) as Alexa, Siri, Cortana and Google Assistant are no less to JARVIS.*


After having been working on NLP problems, I have encountered various situations where I had to refer to a large number of different research papers, NLP blogs and competitions to study about the latest developments.

So, I decided to bring all these resources to one place and make a kick-off digest which would provide the foundation for those who seek to dive deep into NLP.



## 📄 Table of contents

  [1. Introduction](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/tree/master/Introduction)
  
  [2. Data Extraction](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/tree/master/0_Data_Extraction)
  
  [3. Data Preprocessing Cleaning](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/tree/master/1_Data_Preprocessing_Cleaning)
  
  [4. Data Preprocessing Normalization](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/tree/master/2_Data_Preprocessing_Normalization)
  
  [5. PartOfSpeech Tagging](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/tree/master/3_PartOfSpeech_Tagging)
  
  [6. Named Entity Recognition](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/tree/master/4_Named_Entity_Recognition)
  
  [7. Word Embeddings](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/tree/master/5_Word_Embeddings)
  
  [8. Text Summarisation](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/tree/master/Task1_Text_Summarisation)
  
  [9. Text Classification](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/tree/master/Task2_Sentiment_Analysis)
  
  [10. Sentiment Analysis](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/tree/master/Task2_Sentiment_Analysis)
  
 **[Toolbox](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/tree/master/Toolbox)**
 
 **[Data](https://github.com/robagwe/kick-off-NLP-Natural_Language_Processing-Python/tree/master/data)**
 
 
### Key Concepts in NLP

| Concepts | Explanation |
| :---:         |     :---      | 
| Feature   | Any variable that describes the data point, also known as attributes or dimensions. Consider you have customer dataset having customer name (values = Bob, Sam, Jane), Customer City (values = NY, DL, IL), here customer name and customer city are features, also known as attributes or dimensions.    |
|Feature Engineering |The process to create most relevant features from existing features in the dataset to improve accuracy and performance of learning algorithms. Involve add or discard features or derive new feature space. |
|Feature Selection|Creation of subset from the original dataset, means selecting the most useful feature to train, and has lower prediction error than on full model. In this process, some variables are retained or discarded. Common methods for best feature selection are forward elimination, backward elimination etc.|
|Scaling| Features in dataset may vary from different ranges of values, where the highest range of variable could dominate the context of an algorithm or affect the outcome. For e.g. height (range 3 feet to 7 feet), and weight (20 kg to 50 kg). Here both variables to be on right scale to rightly predict the required outcome. Most of the algorithm expect variables to be in common range. Two common approaches to bring features on common scale i.e. normalization and standardization.|
|Noisy Data | Noise is a random error or variance in a measured variable or containing outlier values which deviate from the expected outcome|
|Missing Value |No recorded value for several variables in dataset. Missing values can be filled in through a) manually b) replace with constant value c) most probable value identified using decision tree method etc. |
|Dimension Reduction | Irrelevant or redundant attributes are detected and removed to reduce model complexity.|
|Stop words | Typically adverbs and pronouns are generally classified as stop words, which are filtered out before further processing of text, since these words contribute little to overall meaning e.g. the, a, an|
|Bag of words|A piece of text (sentence or a document) is represented as a bag or multiset of words, disregarding grammar and even word order and the frequency or occurrence of each word is used as a feature for training a classifier.|
|Vector|In text classification first sentence is converted into a computer understandable format which can be thought of as a vector (array) of 0 and 1 with each index representing a word in the training data.|
|NER (Named Entity Recognition)|The process of locating and classifying elements in text into predefined categories such as the names of people, organizations, places, monetary values, percentages, etc.|
|N-grams|Combinations of adjacent words or letters of length n in source text. ‘N’ refers to the number of words or word parts. Find pair of words that occur next to each other. e.g. ‘I work in ValueFirst’ here possible pair could be, ‘I work’ ‘work in’ and so on.|
|TF-IDF|The TF-IDF weighting for a word increases with the number of times the word appears in the document but decreases based on how frequently the word appears in the document set.|

![Rosie](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/2.gif)

## <img src="https://github.com/robagwe/wisdomic-panda/blob/master/imgs/acr.png" width="50">   Hey Buddy!</img>

> :pushpin: **I did my best to cover as many as possible tasks in NLP till now but admittedly this is not "THE ULTIMATE GUIDE". I expect this serve as a starting point when you're about to dig into Natural Language Processing. I'll keep updating this repo myself but what I really hope is you collaborate on this work. If you have any suggestions for more information that should be in this repository or you notice a mistake, please let me know or consider submitting a pull request so others can benefit from your work. Your Contributions are always welcome!:grin: Also, please follow if you'd be interested in reading it. Keep yourself updated with the latest science and technology affairs which will help you with your AI learning initiatives. Thank you very much for reaching out! Please follow if you find it handy and hit :star: to get more kick-off repo updates.**

### Happy Learning!

> *"Never stop fighting until you arrive at your destined place - that is, the unique you. Have an aim in life, continuously acquire knowledge, work hard, and have perseverance to realise the great life." - A. P. J. Abdul Kalam*

