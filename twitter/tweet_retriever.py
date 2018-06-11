import time
from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener
from datetime import datetime


class TweetRetriever(StreamListener):

    def __init__(self, consumer_key, consumer_secret, access_token, access_secret, dump):
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_secret)
        self.api = API(self.auth, wait_on_rate_limit=True)
        self.dump = dump

    def on_status(self, status):
        try:
            print(status)
        except BaseException as e:
            ("[%s] Error on data: %s" % str(datetime.now()), str(e))
        return True

    def on_limit(self, track):
        print("[%s] Rate Limit Exceeded, Sleep for 15 Mins" % str(datetime.now()))
        time.sleep(15 * 60)
        return True

    def on_connect(self):
        print("[%s] Twitter connection stablished" % str(datetime.now()))

    def on_disconnect(self, notice):
        print("[%s] Disconnected by Twitter host: %s" % str(datetime.now()), notice)
        return False

    def on_error(self, status_code):
        print("[%s] Error received from Twitter host: %s" % str(datetime.now()), status_code)
        return True
