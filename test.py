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


if __name__ == "__main__":
    api = setTwitterAuth()
    tweetHelloWorld(api)
