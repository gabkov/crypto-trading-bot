import tweepy
import os
import telegram_channel

consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCES_TOKEN"]
access_token_secret = os.environ["ACCES_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

dgb_list= ["$DGB","$dgb" ,"#DGB", "#dgb" ,"DGB","dgb","DigiByte", "DIGIBYTE", "digibyte"]
positive_list = ["listing", "listed", "add", "added", "adding", "trading", "tradeable", "Listing", "Listed", "Add", "Added", "Adding", "Trading", "Tradeable"]


def poll_tweets_from_user(username):
    try:
        for status in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended").items(5):
            tweet = status.full_text
            if any(word in tweet for word in dgb_list):
                if any(word in tweet for word in positive_list):
                    print("Found a tweet: ")
                    print(tweet)
                    print()
                    telegram_channel.send_message_to_me(f"Found tweet at Segal: \n\n{tweet}")
                    return True
    except Exception as e:
        print(e)
        telegram_channel.send_message_to_me(f"EXCEPTION poll_tweets_from_user({username}):\n{e}")


def poll_tweets_from_cb_accounts(coinbase_acc):
    try:
        for status in tweepy.Cursor(api.user_timeline, screen_name=coinbase_acc, tweet_mode="extended").items(5):
            tweet = status.full_text
            if any(word in tweet for word in dgb_list):
                print("Found a tweet: ")
                print(tweet)
                print()
                telegram_channel.send_message_to_me(f"Found tweet at {coinbase_acc}: \n\n{tweet}")
                return True
    except Exception as e:
        print(e)
        telegram_channel.send_message_to_me(f"EXCEPTION poll_tweets_from_cb_accounts({coinbase_acc}):\n{e}")
