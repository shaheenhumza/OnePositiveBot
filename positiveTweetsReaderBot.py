import os
import tweepy
import random
import time
from classify import *


def setTwitterAuth():
    auth = tweepy.OAuthHandler("RmtBCm2LkNznww3qV0q2Kra7M", "bNFutIDNOJSZ9ENY1DQ1fsMEEbZdYG6kcMF9adn92JurXK086r")
    auth.set_access_token("929349249506201600-kZkbI2rlRsXrj1gmDkqJhSITRHUVSoB", "c0ABYCdIDJJTgFCfgtULY8bgDQt4vHnjipHjkhieIRSo7")
    api = tweepy.API(auth)
    return api

def searchForPositiveTweets(api, searchTerm):
    searchResults = [status for status in tweepy.
                     Cursor(api.search, q=searchTerm).items(100)]
    return searchResults

def writeToFile(searchResults):
    f = open("positiveTweets.txt", "r")
    file = open("positiveTweets.txt", "a")
    for searchResult in searchResults:
        if searchResult.text not in f:
            if(classify(searchResult.text) > 0.25):
                tweet = (searchResult.text).split(" ")
                for word in tweet:
                    if "@" in word:
                        pass
                    elif "http" in word:
                        pass
                    elif "www" in word:
                        pass
                    elif "#" in word:
                        pass
                    elif "RT" in word:
                        pass
                    else:
                        file.write(word + " ")
    file.write("\n")
    f.close()
    file.close()

if __name__ == "__main__":
    api = setTwitterAuth()
    positivewords = [ "stop bullying", "inspiration"
                    , "positivism", "positive thinking", "inspirational"
                    , "kind", "nice", "joke", "funny", "happiness"
                    ,"funny", "purpose", "YOLO", "keep going"
                    ,"never give up", "look ahead", "learn from your mistakes"
                    ,"keep trying", "love", "friend", "friendship", "will to"
                    ,"happy", "positive", "life goal", "light in my"
                    ,"motivational"]

    while True:
        for positiveword in positivewords:
            print (positiveword)
            searchResults = searchForPositiveTweets(api, "\"" + positiveword +"\"")
            writeToFile(searchResults)
            time.sleep(60*2)#two minutes
