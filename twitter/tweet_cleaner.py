import datetime
import time


class TweetCleaner:

    @staticmethod
    def get_adjusted_datetime(gmt_date_time):
        if time.localtime().tm_isdst:
            return gmt_date_time + datetime.timedelta(hours=1)
        else:
            return gmt_date_time.created_at
