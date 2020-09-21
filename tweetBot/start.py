import tweepy
import pandas as pd

CONSUMER_KEY = 'QLYXoiT25b1b61TTWKje8iKJ7'
CONSUMER_SECRET = 'PfkizSsXwWzePXr7L5YUE5w1hVBKAT0PMaA0Cd2KFipNLAW5V0'
ACCESS_TOKEN = '1231594646872219649-ghDhl79wpSivW00dODCTa2xPS63yN8'
ACCESS_SECRET = 'UHkb5JqZ3WGIFB6G0ME9V6lmxNDCPBpRQkpHNTjg93KpQ'

def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    
    #This returns some random tweets from the feed
    '''public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)'''

    #This returns some of the newest tweets from a specified user
    '''vfw = api.user_timeline('')
    for tweet in vfw:
        print(tweet.text)

    def extract_tweet_attributes(tweet_object):
        tweet_list = []

        for tweet in tweet_object:
            tweet_id = tweet.id
            text = tweet.text
            favorite_count = tweet.favorite_count
            retweet_count = tweet.retweet_count
            created_at = tweet.created_at
            source = tweet.source
            tweet_list.append({'tweet_id':tweet_id, 'text':text,  'favorite_count':favorite_count, 'retweet_count':retweet_count, 'created_at':created_at,  'source':source})
        
        df = pd.DataFrame(tweet_list, columns=['tweet_id',
        'text',
        'favorite_count',
        'retweet_count',
        'created_at',
        'source'])

        return df'''

    return api

connect_to_twitter_OAuth()