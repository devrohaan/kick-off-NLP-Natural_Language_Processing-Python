[![Wisdomic Panda](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/panda.png)](http://www.rohanbagwe.com/)  **Wisdomic Panda**
> *Hold the Vision, Trust the Process.*

## Natural Language Processing: A Py Kick-off Digest!
###### Natural Language Processing in Python.

# Text Summarization
*... shortening a text document to create a summary with the major points of the original document.*


**Text Summarization**, consists of picking a subset of a text so that the information disseminated by the subset is as close to the original text as possible. The subset, named the summary, should be human readable.

> :pushpin: Summarization is mainly useful because it condenses information for easier consumption and analysis. 

![TC](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/sum.jpg)
<img src="https://github.com/robagwe/wisdomic-panda/blob/master/imgs/sum.jpg" width="700">

## [Extractive approach Vs Abstractive approach](http://thescipub.com/PDF/jcssp.2016.178.190.pdf)

###### Extractive

This approach entails selecting the X most representative sentences that best cover the whole information expressed by the original text.

### **Graph Base**

The graph base model makes the graph from the document, then summarize it by considering the relation between the nodes (text-unit). TextRank is the typical graph based method.

TextRank is based on PageRank algorithm that is used on Google Search Engine. Its base concept is "The linked page is good, much more if it from many linked page". The links between the pages are expressed by matrix. We can convert this matrix to transition probability matrix by dividing the sum of links in each page. 

TextRank works as follows:

- Pre-process the text: remove stop words and stem the remaining words.
- Create a graph where vertices are sentences.
- Connect every sentence to every other sentence by an edge. The weight of the edge is how similar the two sentences are.

> :bulb: The probability of going from sentence A to sentence B is equal to the similarity of the 2 sentences.

- Run the PageRank algorithm on the graph.
- Pick the vertices(sentences) with the highest PageRank score

In original TextRank the weights of an edge between two sentences is the percentage of words appearing in both of them.

If you want to use TextRank, use:

> - [gensim](https://radimrehurek.com/gensim/summarization/summariser.html)
> - [pytextrank](https://github.com/ceteri/pytextrank)


### **Feature Base**

The feature base model extracts the features of sentence, then evaluate its importance. Here is the list of features that can be used:

- Position of the sentence in input document
- Presence of the verb in the sentence
- Length of the sentence
- TF-IDF
- Named entity tag NE



### **Topic Base**

The topic base model calculates the topic of the document and evaluate each sentences by what kinds of topics are included.

Latent Semantic Analysis (LSA) is usually used to detect the topic. 

The following paper is good starting point to overview the LSA.

:scroll: [Paper Text summarization using Latent Semantic Analysis](https://www.researchgate.net/publication/220195824_Text_summarization_using_Latent_Semantic_Analysis)

#### Implementation:

- [models.lsimodel – Latent Semantic Indexing](https://radimrehurek.com/gensim/models/lsimodel.html)

- [summy](https://github.com/miso-belica/sumy)

## In a nutshell,

> Select relevant phrases of the input document and concatenate them to form a summary.
> :warning: This approach also cannot paraphrase like people sometimes do.

###### Abstractive

This approach builds a summary of the text, in the way a human would build one. We pick ideas from several paragraphs or sentences, build readable sentences and present them in a concise form. 

- Encoder-Decoder Model

:scroll: [Neural Attention Model for Sentence Summarization](https://aclweb.org/anthology/D15-1044)

:scroll: [seq2seq RNN Paper](https://arxiv.org/pdf/1602.06023.pdf)



## Text Summarization Evaluation - BLEU vs ROUGE

#### Rouge-N (recall)

> ### Number of overlapping words (n-grams)/ total words in human reference summary

**Human reference summary:** A good diet must have apples and bananas.

**Machine generated summary:** Apples and bananas are must for a good diet.

 
		ROUGE-1, the score is 7/8 = 0.875.

		For ROUGE-2, it is 4/7 = ~0.57.


###### Generally for summarization evaluation, only ROUGE-1 and ROUGE-2 

> As an example, consider two semantically similar phrases “apples bananas” and “bananas apples”. If we use ROUGE-1 we only consider uni-grams, which are the same for both phrases. But if we use ROUGE-2, we use 2-word phrases, so “apples bananas” become a single entity which is different from “bananas apples”, leading to a “miss” and lower evaluation score.



#### BLEU (precision)

> ### Number of overlapping words (n-grams)/ total words in machine generated summary


**Human reference summary:** A good diet must have apples and bananas.

**Machine generated summary:** Apples and bananas are must for a good diet.

		BLEU is calculated as 7/9 = 0.778

> :pushpin: These results are complementing, as is often the case in precision vs recall. If you have many words from the system results appearing in the human references you will have high Bleu, and if you have many words from the human references appearing in the system results you will have high Rouge.




> #### Extract then Abstract model.
Use extractive model to select the sentence from documents, then adopt the abstractive model to selected sentences.




