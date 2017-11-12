import os
import tweepy
import random
import time
from classify import *
import combineTextFiles


def setTwitterAuth():
    auth = tweepy.OAuthHandler("RmtBCm2LkNznww3qV0q2Kra7M", "bNFutIDNOJSZ9ENY1DQ1fsMEEbZdYG6kcMF9adn92JurXK086r")
    auth.set_access_token("929349249506201600-kZkbI2rlRsXrj1gmDkqJhSITRHUVSoB", "c0ABYCdIDJJTgFCfgtULY8bgDQt4vHnjipHjkhieIRSo7")
    api = tweepy.API(auth)
    return api

def searchForPositiveTweets(api, searchTerm):
    searchResults = [status for status in tweepy.
                     Cursor(api.search, q=searchTerm, lang="en").items(200)]
    return searchResults

def writeToFile(searchResults):
    fileToRead = open("positiveTweets.txt", "r")
    fileToWrite = open("positiveTweets.txt", "a")
    for searchResult in searchResults:
        if searchResult.text not in fileToRead:
            if(classify(searchResult.text) > 0.5):
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
                        fileToWrite.write(word + " ")
    fileToWrite.write("\n")
    fileToRead.close()
    fileToWrite.close()

if __name__ == "__main__":
    api = setTwitterAuth()
    positivewords = [ "stop bullying", "inspiration"
                    , "positivism", "positive thinking", "inspirational"
                    , "happiness" , "purpose", "keep going"
                    ,"never give up", "look ahead", "learn from your mistakes"
                    ,"keep trying", "friendship", "will to"
                    , "positivity", "life goal", "light in my"
                    ,"motivational"]

    while True:
        for positiveword in positivewords:
            print (positiveword)
            searchResults = searchForPositiveTweets(api, "\"" + positiveword +"\"")
            writeToFile(searchResults)
            time.sleep(60*2)#two minutes
        combineTextFiles()
        time.sleep(60*60*3)#sleep for 3 hours
