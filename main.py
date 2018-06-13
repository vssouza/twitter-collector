import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from twitter import TweetRetriever
from log import ScreenLogger

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

dump = ScreenLogger()

tweet_retriever = TweetRetriever(consumer_key, consumer_secret, access_secret, access_secret, dump)

twitter_stream = Stream(auth, tweet_retriever)
twitter_stream.filter(track=['#fortnite'], languages=['en'])
