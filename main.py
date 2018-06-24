import tweepy
import os
from tweepy import OAuthHandler
from tweepy import Stream
from twitter import TweetRetriever
from config import ConfigurationLoader, ConfigUtil


class Main:
    def __init__(self):
        self.config_file_path = os.path.dirname(__file__)
        self.config_file_path = os.path.join(self.config_file_path, "resources", ConfigUtil.CONFIG_FILENAME)
        self.config = ConfigurationLoader(self.config_file_path)
        self.consumer_key = 'YDZ1ka1OjlOpIR8hqx36b28uJ'
        self.consumer_secret = 'gdFvF9fhLenaR6yj4nkUrpRKQwFb8IrHhXGXdmjSkzdLCcCish'
        self.access_token = '999273792030507008-JWCIJtlpW2FDAdEeJkpRvD4nKBdWDij'
        self.access_secret = 'pLp0xdbWbB0Y1zLYKmmzWX2XcBg8qiDcLEZz355V3uPHn'

    def run(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        tweepy.API(auth)
        tweet_retriever = TweetRetriever(self.consumer_key, self.consumer_secret, self.access_secret, self.access_secret)
        twitter_stream = Stream(auth, tweet_retriever)
        twitter_stream.filter(track=['#fortnite'], languages=['en'])


main = Main()
main.run()
