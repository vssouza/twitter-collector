import time
import json
from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener
from datetime import datetime
from log import ConsoleLogger, BaseLogger, FileLogger


class TweetRetriever(StreamListener):

    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_secret)
        self.api = API(self.auth, wait_on_rate_limit=True)
        self.logger = FileLogger(__name__, BaseLogger.INFO, 'log.txt')

    def on_status(self, status):
        try:
            tweet_json = json.dumps(status._json)
            self.logger.info(tweet_json)
        except BaseException as e:
            self.logger.error("[{0}] Error on data: {1}".format(str(datetime.now()), str(e)))
        return True

    def on_limit(self, track):
        self.logger.warning("[{0}] Rate Limit Exceeded, Sleep for 15 Mins".format(str(datetime.now())))
        time.sleep(15 * 60)
        return True

    def on_connect(self):
        self.logger.info("[{0}] Twitter connection stablished".format(str(datetime.now())))

    def on_disconnect(self, notice):
        self.logger.error("[{0}] Disconnected by Twitter host: {1}".format(str(datetime.now()), notice))
        return False

    def on_error(self, status_code):
        self.logger.critical("[{0}] Error received from Twitter host: {1}".format(str(datetime.now()), status_code))
        return False
