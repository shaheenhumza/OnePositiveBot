from secret import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import os
from markovbot import MarkovBot
import tweepy
import random
import time
from classify import *


def setTwitterAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api


def markov():
    tweetbot = MarkovBot()
    dirname = os.path.dirname(os.path.abspath(__file__))
    data1 = os.path.join(dirname, 'positiveTweets.txt')
    data3 = os.path.join(dirname, '10ondate.txt')
    data4 = os.path.join(dirname, 'forCachetes.txt')
    data5 = os.path.join(dirname, 'forCachetes2.txt')
    #data6 = os.path.join(dirname, 'book4.txt')
    #data8 = os.path.join(dirname, 'book4.txt')
    tweetbot.read(data1)
    tweetbot.read(data3)
    tweetbot.read(data4)
    tweetbot.read(data5)
    #tweetbot.read(data6)
    #tweetbot.read(data8)

    my_first_text = tweetbot.generate_text(25, seedword=['life', 'motivation', 'happy', 'dream'])
    print("tweetbot says:")
    print(my_first_text)
    return tweetbot

def getTimeline(api, user):
    lastTweetOfUser = api.user_timeline(user.screen_name, count=1)
    return lastTweetOfUser.text

def searchForNegativeTweets(api, searchTerm):
    allSearchResults = [status for status in tweepy.
                     Cursor(api.search, q=searchTerm).items(100)]
    return allSearchResults


def getUsersToTweet():
    allSearchResults = searchForNegativeTweets(api, "\"depressed\"")
    searchResults = []
    for searchResult in allSearchResults:
        if(classify(searchResult.text) < 0.25):
            searchResults.append(searchResult)
            print((searchResult.user).screen_name)
    return searchResults

def replyToDepressed(api, searchResults):
    for searchResult in searchResults:
        markovBit = tweetbot.generate_text(25, seedword=['happy', 'funny', 'joy', 'love', 'life', 'motivation', 'dream'])
        tweet = "@{} ".format(searchResult.user.screen_name)+ markovBit + " \U0001F916 #OnePositiveBot #StayPositive"
        print(searchResult.id)
        api.update_status(tweet, searchResult.id)
        time.sleep(60*2)


tweetbot = markov()
tweetbot.twitter_login(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

#thread that listens to the target string "depressed" in twitter


#thread that makes the bot tweet something positive automatically every 30s
seeds = ['happy', 'funny', 'joy', 'love']
#tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=1, keywords=seeds, prefix=None, suffix='#OnePositiveBot')

#main thread that choses a random news twitter account and substitutes its last tweet
api = setTwitterAuth()
while True:

    newsAccounts = ["bbcworld", "CNN", "BBCBreaking", "cnnbrk", "SkyNewsBreak"]

    #choose a random news account
    #newsAccount = newsAccounts[random.randint(0, len(newsAccounts) - 1)]
    #get that accounts info and last tweet
    #user = api.get_user(newsAccount)
    #tweet = getTimeline(api, user)
    #print(user.screen_name)

    #generate reply to tweet
    searchResults = getUsersToTweet()
    replyToDepressed(api, searchResults)
    time.sleep(60*60*3) #sleep for 3 hours
