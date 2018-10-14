[![Wisdomic Panda](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/panda.png)](http://www.rohanbagwe.com/)  **Wisdomic Panda**
> *Hold the Vision, Trust the Process.*

## Natural Language Processing: A Py Kick-off Digest! 

###### Natural Language Processing in Python.

# Introduction
*... a machine’s ability to ingest what is said to it, break it down, comprehend its meaning, determine appropriate action, and respond back in language the user will understand.*

#### “Natural Language” means a language that is used for everyday communication by humans; languages such as English, Hindi, or Spanish. In contrast to artificial languages such as programming languages and mathematical notations, natural languages have evolved as they pass from generation to generation, and are hard to pin down with explicit rules. 

![NLP](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/3.gif)

##### *Natural Language Processing is basically computer manipulation of natural language. At one extreme, it could be as simple as counting word frequencies to compare different writing styles. At the other extreme, NLP involves “understanding” complete human utterances.We interact with technology every single day of our lives, but humans and computers communicate in fundamentally different ways. Whereas we tell stories, take notes, and relay information through a narrative, computers rely on objective data, commands and hence reply on 0 and 1.*


> :pushpin: NLP began in earnest in 1950 when Alan Turing published his paper entitled “Computing Machinery and Intelligence,” from which the so-called Turing Test emerged. Turing basically asserted that a computer could be considered intelligent if it could carry on a conversation with a human being without the human realizing they were talking to a machine. The goal of natural language processing is to allow that kind of interaction so that non-programmers can obtain useful information from computing systems. Sometimes NLP is confused with Machine Learning (ML), but this is just because some tools from ML are applied to NLP to improve the field.
ML as a set of tools such that some of this tools are useful to solve NLP tasks. Deep Learning (DL) is a branch of ML that makes use of a specific type of architectures or models named Neural Networks to solve different NLP tasks.





## DIFFERENCE BETWEEN NLP, AI, ML, DL & NN

**AI or Artificial Intelligence** – Building systems that can do intelligent things.

**NLP or Natural Language Processing** – Building systems that can understand language. It is a subset of Artificial Intelligence.

**ML or Machine Learning** – Building systems that can learn from experience. It is also a subset of Artificial Intelligence.

**NN or Neural Network** – Biologically inspired network of Artificial Neurons.

**DL or Deep Learning** – Building systems that use Deep Neural Network on a large set of data. It is a subset of Machine Learning.

## In a nutshell,

> *"It looks plain text to human and binary to machine."*- a layman!

> *"It is similar to other ML algorithms with just extra flavor to convert text part into matrix of feature according to requirements with mamy methods and then applying any other ML algorithm to train model to give fruitful result."*- an Engineer!

> *"It's a collection of many words as a feature for every sentence in a paragraph by constructing some tf-idf matrix against features and calculating similarity between words using methods such as euclidean distance, cosine similarly, etc again depending on requirements to predict, suggest, pointing odd one out, etc words."*- a Data Scientist!

NLP deal with different aspects of language such as:

**Phonology** – It is systematic organization of sounds in language.

**Morphology** – It is a study of words formation and their relationship with each other.

###### :pushpin:This digest mainly focuses on Natural Language Processing on data in Texual form.

Before moving further, I would like to briefly explain some of the fundamental NLP tasks that are included in this digest:


| **NLP Tasks**     | **Technique**    | **Input** |   **Output**  |
| ------------- | ------------- | ----- | :-----------: |
| Sentence Segmentation | identifies sentence boundaries in the given text i.e where one sentence ends and where another sentence begins.| Alex met CR7. He said "Hi! What’s up Cristiano?" | `Sentence 1 – Alex met CR7.` `Sentence 2 – He said "Hi! What’s up Cristiano?"` |
|  Tokenization      | identifies different words, numbers, and other punctuation symbols.      |  He said "Hi! What’s up Cristiano?" | `[He] [said] ["] [Hi] [!] [What] [‘][s] [up][Cristiano] [?] ["] `|
| Stemming | process of eliminating affixes (suffixed, prefixes, infixes, circumfixes) from a word (“ing”, “ly”, “es”, “s” etc) in order to obtain a word stem.|    drinking |`drink`      |
| Lemmatization | process of obtaining the root form of the word. |    drink, drank, drunk | `drink`  |
| Part-of-Speech tagging | assigns each word in a sentence its respective part-of-speech tag such as designating word as noun or adverb.| CR7 loves football |`CR7: N – Noun form` `Loves: VB – Verb base form` `football: N – Noun form`      |
| Parsing | involves the analysis of words in the sentence for grammar and their arrangement in a manner that shows the relationships among the words  |Vidic and Ferdinand went into a bar. | `(S(NP(NP Vidic) and (NP(Ferdinand))(VP(went (PP into (NP a bar))))`|
| Named Entity Recognition  | identifies entities such as persons, location and time within the documents. | Let’s meet sir Alex at 6 am at old trafford. |`Person: Alex ` `Time: 6 am` `Location: old trafford`| 
| Co-Reference Resolution   | process of defining the relationship of given word in a sentence with a previous and the next sentence. |    CR7 loves football. He lives football |`[HE - CR7]`|


## Natural Language Understanding


**Natural Language Understanding** is a subset of NLP that deals with the much narrower, but equally important facet of how to best handle unstructured inputs and convert them into a structured form that a machine can understand and act upon. While humans are able to effortlessly handle mispronunciations, swapped words, contractions, colloquialisms, and other quirks, machines are less adept at handling unpredictable inputs.
It undertakes the analysis of content, text-based metadata and generates summarized content in natural, human language. It is opposite to the process of Natural Language Generation. NLG deals with input in the form of data and generates output in the form of plain text while Natural Language Understanding tools process text or voice that is in natural language and generates appropriate responses by summarizing, editing or creating vocal responses.

To site an example,
    
 > Input: :cold_sweat::scream: You Killed it brother!!
   
 > Input: You killed it on stage brother!!:star2::boom::guitar:
    
    Humans can easily figure out the difference but what about machines ...?
     

So, what does it mean to understand language? Well, simply put, it means that you can understand the relationship between words and the objects they refer to. Then the next question is, what does it take to understand these relationships? It requires what we call “world knowledge”. The words only represent concepts, but a system that can understand language needs to understand what these concepts mean.

Obtaining world knowledge means that we need to be able to identify and segment what information we receive so that we can properly bin it into categories in our brain. There are many ways for us to obtain this world information as well. We take in data through all of our senses, and computers don’t have access to this type of data the same way we do.

**"Hence, this knowledge of the world must be taught if we expect machine to emulate super intelligence! This includes every possible minute detail of life or hunan civilization that we have been trained on while living our time. And thus to best of my knowledge I would like to conclude that it shall be 'The Achievement' of the mankind.  As ____ created Humans, Humans created Robots! And I hope this chain evolves in time."**


------



## Key Applications of NLP
 ###### NLP is getting a lot of importance due to the recent boom of the so-called chatbots or conversational agents in several industries.The study of natural language has a long past and these agents are not the first important application. Here are multiple ways NLP is used today:These are some successful implementations of natural language processing!

- Search engines like Google, Yahoo, etc. Google's search engine understands that you are a tech guy, so it shows you results related to that. Google and Bing and other search systems use NLP to extract terms from text to populate their indexes and to parse search queries.

-	Google Translate applies machine translation technologies in not only translating words, but in understanding the meaning of sentences to provide a true translation.

- Social website feeds like your Facebook news feed. The news feed algorithm understands your interests using natural language processing and shows you related ads and posts more likely than other posts.

- Speech engines like Apple Siri.
**Since the invention of the typewriter, the keyboard has been the king of human-computer interface. But today with voice recognition via  virtual assistants,like Amazon’s Alexa, Google’s Now, Apple’s Siri and Microsoft’s Cortana respond to vocal prompts and do everything from finding a coffee shop to getting directions to our office and also tasks like turning on the lights in home, switching the heat on etc.**

-  **Text classification** 
Spam filters like Google spam filters. It's not just about your usual spam filtering; now, spam filters understand what's inside the email content and see if it's spam or not.

- The most basic and well known application of NLP is Microsoft Word spell checking.

- Text analysis, also known as sentiment analytics is a key use of NLP. Businesses are most concerned with comprehending how their customers feel emotionally and use that data for betterment of their service.

- **Information Extraction** 
Information extraction is something which proposes email program to automatically add events to the calendar.
Email filters are another important application of NLP. By analyzing the emails that flow through the servers, email providers can calculate the likelihood that an email is spam based its content by using Bayesian or Naive based spam filtering.
 

- Many important decisions in financial markets use NLP by taking plain text announcements, and extracting the relevant info in a format that can be factored into algorithmic trading decisions. E.g. news of a merger between companies can have a big impact on trading decisions, and the speed at which the particulars of the merger, players, prices, who acquires who, can be incorporated into a trading algorithm can have profit implications in the millions of dollars. **Multiple software products and platforms are now available that analyse market movements, the profile of industries and financial strength of a company and based on technical analysis design the trading patterns. Advanced Natural Language Understanding tools which scan through various sources like financial statements, reports, market news are the basis of automated trading systems.**


- **Question Answering**
IBM Watson is the most prominent example of question answering via information retrieval that helps guide in various areas like healthcare, weather, insurance etc.


- **Sentimental analysis** 
Most of the real customer sentiments hence are trapped in unstructured data. News, blog posts, chats, and social media updates contain huge amounts of such data which is more natural and can be used to know the ‘real’ feelings of customers about the product or service. Natural language understanding software products help businesses to scan through such scattered data and draw practical inferences.
It is done on the given text to predict the subject of the text eg: whether the text conveys judgment, opinion or reviews etc.

- **Conversational Agents** 
Think of the usual customer experience you get at a restaurant: book a table, get to the place, order a meal, wait for the food, enjoy when it finally arrives, and pay a check. Why not use a simple chatbot to cut down on waiting at every stage (apart from enjoying your meal, I guess)?
Take a Burger King bot for example. It acts as a virtual waiter that takes your order in advance, helps you pick the restaurant closest to you and make an in-app payment. All you need to do is go and grab your delicious Whopper.

- **Automatic summarizer** 
Given the input text, the task is to write a summary of text discarding irrelevant points.


 > :pushpin: Apart from application in Big Data, Log Mining, and Log Analysis it has other major application areas. Although the term ‘NLP’ is not as popular as ‘big data’ ‘machine learning’ but we are using NLP every day.







