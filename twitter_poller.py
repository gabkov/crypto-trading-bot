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


#DCR (BTC nagyobb volume)?!
tickers = ['MATIC', 'OCEAN', 'STORJ', 'THETA', 'WAVES', 'DOGE', 'HBAR',
'IOST', 'IOTA', 'KAVA', 'LEND', 'NANO', 'QTUM', 'ADA', 'ANT', 'BAL',
'BNT', 'BTS', 'BTT', 'CRV', 'DCR', 'DGB', 'DOT', 'ENJ', 'ERD',
'FET', 'HOT', 'ICX', 'JST', 'KMD', 'LSK', 'MFT', 'NEO', 'OGN', 'ONE',
'ONT', 'REN', 'RLC', 'RSR', 'RVN', 'SNX', 'SOL', 'SRM', 'STX', 'SXP', 'TRX',
'VET', 'XMR', 'YFI', 'ZEN', 'ZIL', 'SC']


def poll_tweets_from_cb_accounts(coinbase_acc):
    try:
        for status in tweepy.Cursor(api.user_timeline, screen_name=coinbase_acc, tweet_mode="extended").items(5):
            tweet = status.full_text
            res = [ticker for ticker in tickers if(ticker in tweet)]
            if res:
                symbol = res[0]
                print(f"Found a tweet for symbol: {symbol}")
                print(tweet)
                print()
                telegram_channel.send_message_to_me(f"Found tweet for symbol {symbol} at {coinbase_acc}: \n\n{tweet}")
                return res
        return []
    except Exception as e:
        print(e)
        telegram_channel.send_message_to_me(f"EXCEPTION poll_tweets_from_cb_accounts({coinbase_acc}):\n{e}")
