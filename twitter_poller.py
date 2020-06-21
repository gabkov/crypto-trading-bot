import tweepy
import os

consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCES_TOKEN"]
access_token_secret = os.environ["ACCES_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

dgb_list= ["$DGB","$dgb" ,"#DGB", "#dgb" ,"DGB","dgb","DigiByte", "DIGIBYTE", "digibyte"]
positive_list = ["listing", "listed", "add", "added", "adding", "trading", "tradeable", "Listing", "Listed", "Add", "Added", "Adding", "Trading", "Tradeable"]


def poll_tweets():
    for status in tweepy.Cursor(api.user_timeline, screen_name='@zosegal',tweet_mode="extended").items(5):
        tweet = status.full_text
        if any(word in tweet for word in dgb_list):
            if any(word in tweet for word in positive_list):
                print("Found a tweet: ")
                print(tweet)
                print()
                return True