from secret import *
import tweepy
from classify import *

def setTwitterAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api


def searchTweet(api, searchTerm):
    searchResults = [status for status in tweepy.
                     Cursor(api.search, q=searchTerm).items(100)]
    return searchResults

if __name__ == "__main__":
	api = setTwitterAuth()
	keyword = "depressed"
	searchResults = searchTweet(api, "\"" + keyword +"\"")
	for item in searchResults:
		if(classify(item.text) < -0.5):
			print item.text
			print classify(item.text)
