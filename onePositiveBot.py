from secret import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import os
from markovbot3 import MarkovBot
import tweepy
import random
import time
from classify import *
from stringReplacement import filter


def setTwitterAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api


def markov():
    tweetbot = MarkovBot()
    dirname = os.path.dirname(os.path.abspath(__file__))
    data = os.path.join(dirname, 'trainingData.txt')
    tweetbot.read(data)
    return tweetbot

def getTimeline(api, user):
    lastTweetOfUser = api.user_timeline(user.screen_name, count=1)
    return lastTweetOfUser[0]

def searchForNegativeTweets(api, searchTerm):
    allSearchResults = [status for status in tweepy.
                     Cursor(api.search, q=searchTerm).items(100)]
    return allSearchResults


def getUsersToTweet():
    allSearchResults = searchForNegativeTweets(api, "\"depressed\"")
    searchResults = []
    for searchResult in allSearchResults:
        if(classify(searchResult.text) < 0):
            searchResults.append(searchResult)
            print((searchResult.user).screen_name)
    return searchResults

def replyToDepressed(api, searchResults):
    for searchResult in searchResults:
        markovBit = tweetbot.generate_text(25, seedword=['life', 'joy', 'love', 'funny', 'happy', 'motivation', 'dream'])
        tweet = "@{} ".format(searchResult.user.screen_name)+ markovBit + " \U0001F916 #OnePositiveBot #StayPositive"
        print(searchResult.id)
        api.update_status(tweet, searchResult.id)
        time.sleep(60*3)

def replyToNewsAccount(api):
    #choose a random news account
    newsAccounts = ["bbcworld", "CNN", "BBCBreaking", "cnnbrk", "SkyNewsBreak"]
    newsAccount = newsAccounts[random.randint(0, len(newsAccounts) - 1)]
    #get that accounts info and last tweet

    user = api.get_user(newsAccount)
    tweet = getTimeline(api, user)
    print(user.screen_name)
    reply = "@{} ".format(user.screen_name) + filter(tweet.text) + " \U0001F916 #OnePositiveBot #NewsMadePositive"
    api.update_status(reply, tweet.id)


tweetbot = markov()
tweetbot.twitter_login(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

#thread that listens to the target string "#AskOnePositiveBot" in twitter
targetstring = 'AskOnePositiveBot'
keywords = ['ask', 'life', 'positive', 'dream', 'purpose']
prefix = None
suffix = ' \U0001F916 #OnePositiveBot'
maxconvdepth = 2
tweetbot.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)



#thread that makes the bot tweet something positive automatically every 30s
seeds = ['happy', 'funny', 'joy', 'love']
tweetbot.twitter_tweeting_start(days=0, hours=4, minutes=15, keywords=seeds, prefix=None, suffix=' \U0001F916 #OnePositiveBot')


#main thread that choses a random news twitter account and substitutes its last tweet
api = setTwitterAuth()
while True:

    #generate reply to tweet
    searchResults = getUsersToTweet()
    replyToDepressed(api, searchResults)
    time.sleep(60*10) #sleep for 10 minuts

    replyToNewsAccount(api)
    time.sleep(60*5)

tweetbot.twitter_autoreply_stop()
tweetbot.twitter_tweeting_stop()
