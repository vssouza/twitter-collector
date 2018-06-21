import time
import json
import logging
from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener
from datetime import datetime


class TweetRetriever(StreamListener):

    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_secret)
        self.api = API(self.auth, wait_on_rate_limit=True)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def on_status(self, status):
        try:
            tweet_json = json.dumps(status._json)
            self.logger.info(tweet_json)
        except BaseException as e:
            "[{0}] Error on data: {1}".format(str(datetime.now()), str(e))
        return True

    def on_limit(self, track):
        print("[{0}] Rate Limit Exceeded, Sleep for 15 Mins".format(str(datetime.now())))
        time.sleep(15 * 60)
        return True

    def on_connect(self):
        print("[{0}] Twitter connection stablished".format(str(datetime.now())))

    def on_disconnect(self, notice):
        print("[{0}] Disconnected by Twitter host: {1}".format(str(datetime.now()), notice))
        return False

    def on_error(self, status_code):
        print("[{0}] Error received from Twitter host: {1}".format(str(datetime.now()), status_code))
        return False
