import nltk
from textblob import TextBlob

def classify(text):
	blob = TextBlob(text)
	return blob.sentiment.polarity