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

def searchUsersFor(api, keyword):
	f = open("usersToTweetTo.txt", "a")
	searchResults = searchTweet(api, "\"" + keyword +"\"")
	for item in searchResults:
		if(classify(item.text) < -0.5):
			f.write(item.user.screen_name)
			f.write(" ")
			f.write(str(item.id))
			f.write("\n")



api = setTwitterAuth()
searchUsersFor(api, "depressed")
print "finisheasasd"
f = open("usersToTweetTo.txt", "a")
f.write("----------------------")
searchUsersFor(api, "suicide")