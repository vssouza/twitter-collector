from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor


class TweetRetriever:

    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_secret)
        self.api = API(self.auth, wait_on_rate_limit=True)

    def get_tweets_by_hashtag(self, hashtag_filters, tweet_count=0, tweet_lang='en'):
        list_of_tweets = []
        query_filter = self.build_hashtag_filter(hashtag_filters)
        for tweet in Cursor(self.api.search, q=query_filter, count=tweet_count, lang=tweet_lang).items():
            list_of_tweets.append(tweet)
        return list_of_tweets

    @staticmethod
    def build_hashtag_filters(self, hashtag_filter_groups):
        query_filter = ''
        for (index, hashtag_filter_group) in enumerate(hashtag_filter_groups):
            query_filter += self.build_hashtag_and_group(hashtag_filter_group)
            if index < (hashtag_filter_groups.__len__ - 1):
                query_filter += '+OR+'

    @staticmethod
    def build_hashtag_and_group(self, hashtag_filter_group):
        query_filter = ''
        for (index, hashtag) in enumerate(hashtag_filter_group):
            query_filter += hashtag
            if index < (hashtag_filter_group.__len__ - 1):
                query_filter += '+AND+'
