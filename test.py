from secret import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import os
#from markovbot import MarkovBot
import tweepy
import random

def setTwitterAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def tweetHelloWorld(api):
    api.update_status("Hello, World! #{}"
                      .format(random.randint(0, 10000)))

def searchTweet(api, searchTerm):
    searchResults = [status for status in tweepy.
                     Cursor(api.search, q=searchTerm).items(100)]
    return searchResults

def replyToTweet(api, searchResults):
    randomTweet = searchResults[random.randint(0, len(searchResults) - 1)]
    tweet = ("@{} This is a demo search for our bot. Please dont use that language #{}"
            .format(randomTweet.user.screen_name,
            random.randint(0, 10000)))
    tweetID = randomTweet.id
    api.update_status(tweet, tweetID)


if __name__ == "__main__":
    api = setTwitterAuth()
    keyword = "fuck"
    searchResults = searchTweet(api, "\"" + keyword +"\"")
    replyToTweet(api, searchResults)
