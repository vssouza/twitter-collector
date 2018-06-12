import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from twitter import TweetRetriever
from storage import ScreenStorage

consumer_key = ''
consumer_secret = ''
access_secret = ''
access_token = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

dump = ScreenStorage()

tweet_retriever = TweetRetriever(consumer_key, consumer_secret, access_secret, access_secret, dump)

twitter_stream = Stream(auth, tweet_retriever)
twitter_stream.filter(track=['#fortnite'], languages=['en'])
