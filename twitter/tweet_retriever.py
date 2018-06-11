from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener
from time import sleep


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
            print("Error on data: %s" % str(e))
        return True

    def on_limit(self, track):
        print("Rate Limit Exceeded, Sleep for 15 Mins")
        sleep(15 * 60)
        return True

    def on_error(self, status_code):
        print("Error received %s" % status_code)
        return True
