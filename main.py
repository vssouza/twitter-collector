import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from twitter import TweetRetriever

consumer_key = 'YDZ1ka1OjlOpIR8hqx36b28uJ'
consumer_secret = 'gdFvF9fhLenaR6yj4nkUrpRKQwFb8IrHhXGXdmjSkzdLCcCish'
access_token = '999273792030507008-JWCIJtlpW2FDAdEeJkpRvD4nKBdWDij'
access_secret = 'pLp0xdbWbB0Y1zLYKmmzWX2XcBg8qiDcLEZz355V3uPHn'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

tweet_retriever = TweetRetriever(consumer_key, consumer_secret, access_secret, access_secret)

twitter_stream = Stream(auth, tweet_retriever)
twitter_stream.filter(track=['#fortnite'], languages=['en'])
