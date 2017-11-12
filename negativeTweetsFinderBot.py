from secret import *
import tweepy
from classify import *
import time

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
    searchResults = searchTweet(api, "\"" + keyword +"\"")
    usersToTweet = []
    for searchResult in searchResults:
        if(classify(searchResult.text) < -0.5):
            usersToTweet.append(searchResult.user.screen_name + " "
                                + )
            print((item.user).screen_name)
    return usersToTweet


api = setTwitterAuth()
while True:
    searchUsersFor(api, "depressed")
    time.sleep(60)
