# VADER Sentiment Analysis: An NLP Approach to Evaluate Emotions in Text

This code is a sentiment analysis implementation using the Natural Language Toolkit (nltk) library in Python. The aim of the code is to analyze the sentiment of a given text file and classify it as Positive, Neutral, or Negative based on the sentiment intensity of each word.

## Libraries
- **string** - used for string operations (e.g., removing punctuation marks)    
- **nltk** - Natural Language Toolkit library used for sentiment analysis, tokenization, and word processing   
- **nltk.sentiment.vader** - used for sentiment analysis using the VADER (Valence Aware Dictionary and Sentiment Reasoner) algorithm   
- **nltk.tokenize** - used for tokenizing the text into words   
- **nltk.corpus** - used for downloading the stopwords corpus   
- **nltk.stem** - used for performing word stemming   

## Downloads
Before using the code, it is necessary to download the following libraries using **nltk.download**:  
 
- **vader_lexicon** - used for sentiment analysis using the VADER algorithm   
- **punkt** - used for tokenizing the text into words    
- **stopwords** - used for removing stop words from the text   
- **wordnet** - used for performing word stemming    

## Class SentimentAnalysis

The Sentiment Analysis class contains the following functions to perform the sentiment analysis:   

- **__init__(self, file_path)** - initializes the class with the file path and calls the read_file, process_text, and analyze_sentiment functions to perform the sentiment analysis   
- **read_file(self)** - reads the text from the file and returns it as a string. If the file is not found, it returns an empty string   
- **process_text(self)** - pre-processes the text to remove punctuation, convert to lower case, remove stop words, and perform word stemming. The processed text is returned as a string   
- **analyze_sentiment(self)** - analyzes the sentiment intensity of each word in the processed text using the VADER algorithm and returns a list of sentiments   
- **classify_sentiment(self)** - classifies the overall sentiment as Positive, Neutral, or Negative based on the compound score of the sentiments   

## Testing the code

To test the code, you need to provide a text file (sample_text.txt in this example). The code creates an object of the SentimentAnalysis class with the file path and prints the sentiments of each word and the overall sentiment.   
