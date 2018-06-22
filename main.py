import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from twitter import TweetRetriever

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

tweet_retriever = TweetRetriever(consumer_key, consumer_secret, access_secret, access_secret)

twitter_stream = Stream(auth, tweet_retriever)
twitter_stream.filter(track=['#fortnite'], languages=['en'])
