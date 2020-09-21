import tweepy

CONSUMER_KEY = 'QLYXoiT25b1b61TTWKje8iKJ7'
CONSUMER_SECRET = 'PfkizSsXwWzePXr7L5YUE5w1hVBKAT0PMaA0Cd2KFipNLAW5V0'
ACCESS_TOKEN = '1231594646872219649-ghDhl79wpSivW00dODCTa2xPS63yN8'
ACCESS_SECRET = 'UHkb5JqZ3WGIFB6G0ME9V6lmxNDCPBpRQkpHNTjg93KpQ'

class TwitterBot:

    def __init__(self, main):
        self.main = main

        self.authenticate()

        #self.post_tweet()

        #self.see_tweets()

        #self.unfollow_everyone()
        
        #self.get_mentions()

        #self.see_fren()



    def authenticate(self):
        """This handles the authentication part of the bot"""
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        self.api = tweepy.API(self.auth)

        #self.api.user_timeline(id='zetsusama2')
        #self.tweepy.Cursor(api.user_timeline, id='zetsusama2')

    def post_tweet(self):
        """This function is used to post tweets!"""
        tweet = input('Digite o que deseja que fique no tweet: ')
        self.api.update_status(tweet)
        print('Chegou aqui')

    def see_tweets(self):
        """This function is used to see the tweets of a certain user, if no user is selected, it'll just retrieve
        the latest tweets from the profile"""
        user = self.api.user_timeline('andretxiz') #Insert the username in here
        for tweet in user:
            print(tweet.text)

        """Inside this function there will be a new dataframe made with pandas, this is usually most useful for
        data analysis, so Imma comment the function and whenever it needs to be used, just de-comment it."""
        '''

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

        return df
        
        Notice that you should import pandas as pd before using this function, also, there are other
        attributes that can be used.'''

    def unfollow_everyone(self):
        #Unfollow everyone
        userfrens = self.api.friends_ids()
        for fren in userfrens:
            self.api.destroy_friendship(f'{fren}')

    def get_mentions(self):
        #Get the mentions
        tweet_mentions = []
        for mentions in tweepy.Cursor(self.api.mentions_timeline).items():
            tweet_mentions.append(mentions.author.screen_name)
            tweet_mentions.append(mentions.text)
            
        #Get the user and its tweet when mentioned
        for mention in range(0, len(tweet_mentions), 2):
            print(f'{tweet_mentions[mention]} : {tweet_mentions[mention+1]}')
        #PAREI AQUI

    def see_fren(self):
        friends = []
        for friend in self.api.friends_ids():
            friends.append(friend)
        print(friends)

    def show_fren(self):
        print(self.api.lookup_friendships('4795887437', M))

    def Malu(self):

        self.api.retweet('PRECISO DO ID DO TWEET DELA')

twApp = TwitterBot
twApp('app')
