from pymongo import MongoClient


class TweetMongoDB:

    tweet_collection = 'tweet'
    hashtag_collection = 'hashtag'

    def __init__(self, url, port, database, username, password):
        self.url = url
        self.port = port
        self.username = username
        self.password = password
        self.address = 'mongodb://%s:%s@%s:%s?authMechanism=SCRAM-SHA-1', self.username, self.password, self.url, self.port, self.database
        self.client = MongoClient(self.address)
        self.database = self.client[database]

    def close_connection(self):
        self.client.close(self)

    def add_hashtag(self, hashtag):
        self.database[self.hashtag_collection].insert_one(hashtag).inserted_id

    def add_raw_tweet(self, tweet):
        return self.database[self.tweet_collection].insert_one(tweet).inserted_id

    def remove_hashtag(self, hashtag_id):
        self.database[self.hashtag_collection].remove(hashtag_id)

    def remove_raw_tweet(self, tweet_id):
        self.database[self.tweet_collection].remove(tweet_id)

    def list_raw_tweets(self, limit=0):
        if limit > 0:
            return self.database[self.tweet_collection].find().limit(limit)
        else:
            return self.database[self.tweet_collection].find()

    def list_hashtags(self, limit=0):
        if limit > 0:
            return self.database[self.hashtag_collection].find().limit(limit)
        else:
            return self.database[self.hashtag_collection].find()
