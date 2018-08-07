import tweepy
import os
from tweepy import OAuthHandler
from tweepy import Stream
from twitter import TweetRetriever
from config import ConfigurationLoader, ConfigUtil


class Main:
    def __init__(self):
        self._config_file_path = os.path.dirname(__file__)
        self._config_file_path = os.path.join(self._config_file_path, "resources", ConfigUtil.CONFIG_FILENAME)
        self._config = ConfigurationLoader(self._config_file_path)
        self._twitter_config = self._config.get_twitter_config()
        self._consumer_key = self._twitter_config["consumerkey"]
        self._consumer_secret = self._twitter_config["consumersecret"]
        self._access_token = self._twitter_config["accesstoken"]
        self._access_secret = self._twitter_config["accesssecret"]
        self._hash_tag = self._twitter_config["hashtag"]
        self._language = self._twitter_config["language"]

    def run(self):
        auth = OAuthHandler(self._consumer_key, self._consumer_secret)
        auth.set_access_token(self._access_token, self._access_secret)
        tweepy.API(auth)
        tweet_retriever = TweetRetriever(self._consumer_key, self._consumer_secret, self._access_secret, self._access_secret)
        twitter_stream = Stream(auth, tweet_retriever)
        twitter_stream.filter(track=[self._hash_tag], languages=[self._language])


main = Main()
main.run()
