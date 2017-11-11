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



def markov():
    tweetbot = MarkovBot()
    dirname = os.path.dirname(os.path.abspath(__file__))
    data1 = os.path.join(dirname, 'positiveTweets.txt')
    data2 = os.path.join(dirname, '1liner.txt')
    data3 = os.path.join(dirname, '10ondate.txt')
    data4 = os.path.join(dirname, 'forCachetes.txt')
    #data5 = os.path.join(dirname, 'book3.txt')
    #data6 = os.path.join(dirname, 'book4.txt')
    data7 = os.path.join(dirname, 'jokes.txt')
    #data8 = os.path.join(dirname, 'book4.txt')
    tweetbot.read(data1)
    tweetbot.read(data2)
    tweetbot.read(data3)
    tweetbot.read(data4)
    #tweetbot.read(data5)
    #tweetbot.read(data6)
    tweetbot.read(data7)
    #tweetbot.read(data8)

    my_first_text = tweetbot.generate_text(25, seedword=['life', 'motivation', 'happy', 'bullying'])
    print("tweetbot says:")
    print(my_first_text)

if __name__ == "__main__":
    markov()
