import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from twitter import TweetRetriever

consumer_key = 'mppcFHvYdXtzshV89ppzBmdTR'
consumer_secret = '9H1OwHwBhHWKQBV8gPj1hbHpTtJF13tHmyzCUArB1DDK5POkPu'
access_secret = 'Ddc18lswGpBM33IDWezEWsccHyud6Bx4kUH5gP3KQ2rcg'
access_token = '999273792030507008-2PR0utUvBFHwFebYhOCJt7ATn9FKmSc'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

tweet_retriever = TweetRetriever(consumer_key, consumer_secret, access_secret, access_secret, 'temp')

twitter_stream = Stream(auth, tweet_retriever)
twitter_stream.filter(track=['#fortnite'])


