from secret import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import os
from markovbot import MarkovBot
import tweepy
import random


def setTwitterAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def searchForPositiveTweets(api, searchTerm):
    searchResults = [status for status in tweepy.
                     Cursor(api.search, q=searchTerm).items(100)]
    return searchResults

def writeToFile(searchResults):
    file = open("positiveTweets.txt", "a")
    for searchResult in searchResults:
        words = (searchResult.text).split(" ")
        for word in words:
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

def combineTextFiles():
    file = open("everything.txt", "a")

    file0 = open('positiveTweets.txt', 'r')
    for line in file0:
        file.write(line + "\n")

    #file1 = open('book1.txt', 'r')
    #for line in file1:
    #    file.write(line + "\n")

    file2 = open('1liner.txt', 'r')
    for line in file2:
        file.write(line + "\n")

    file3 = open('10ondate.txt', 'r')
    for line in file3:
        file.write(line + "\n")

    file4 = open('jokes.txt', 'r')
    for line in file4:
        file.write(line)

    file5 = open('book1.txt', 'r')
    for line in file5:
        file.write(line)

    file6 = open('book3.txt', 'r')
    for line in file6:
        file.write(line)

    file7 = open('book4.txt', 'r')
    for line in file7:
        file.write(line)






def markov():
    tweetbot = MarkovBot()
    dirname = os.path.dirname(os.path.abspath(__file__))
    combineTextFiles()
    data = os.path.join(dirname, 'everything.txt')
    tweetbot.read(data)

    my_first_text = tweetbot.generate_text(25, seedword=[u'positive', u'purpose', u'motivation', u'happy'])
    print("tweetbot says:")
    print(my_first_text)

if __name__ == "__main__":
    positivewords = ["anti bullying", "stop bullying", "inspiration"
                    , "positivism", "positive thinking", "racism"
                    , "inspirational", "kind", "nice", "#joke", "funny"]
    for positiveword in positivewords:
        api = setTwitterAuth()
        searchResults = searchForPositiveTweets(api, "\"" + positiveword +"\"")
        writeToFile(searchResults)
        markov()
