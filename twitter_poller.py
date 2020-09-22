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


tickers = ['COCOS', 'MATIC', 'OCEAN', 'STORJ', 'STORM', 'STRAT', 'SUSHI', 'TFUEL', 'THETA', 
'WAVES', 'AION', 'ANKR', 'ARDR', 'ARPA', 'AVAX', 'BEAM', 'BZRX', 'CELR', 'COTI', 
'CTSI', 'CTXC', 'DATA', 'DENT', 'DOCK', 'DOGE', 'DREP', 'DUSK', 'EGLD', 'HBAR', 
'HIVE', 'IOST', 'IOTA', 'IOTX', 'IRIS', 'KAVA', 'LEND', 'LUNA', 'MITH', 'NANO', 
'NPXS', 'NULS', 'PAXG', 'PERL', 'QTUM', 'RUNE', 'SAND', 'STMX', 'STPT', 'TOMO', 
'TROY', 'VITE', 'VTHO', 'WING', 'WNXM', 'YFII', 'ADA', 'ANT', 'BAL', 'BCC', 'BEL', 
'BLZ', 'BNB', 'BNT', 'BSV', 'BTS', 'BTT', 'CHR', 'CHZ', 'COS', 'CRV', 'DCR', 'DGB', 
'DIA', 'DOT', 'ENJ', 'ERD', 'FET', 'FIO', 'FTM', 'FTT', 'FUN', 'GTO', 'GXS', 'HOT', 
'ICX', 'JST', 'KEY', 'KMD', 'KSM', 'LSK', 'LTO', 'MBL', 'MCO', 'MDT', 'MFT', 'MTL', 
'NBS', 'NEO', 'NKN', 'OGN', 'ONE', 'ONG', 'ONT', 'OXT', 'PNT', 'REN', 'RLC', 'RSR', 
'RVN', 'SNX', 'SOL', 'SRM', 'STX', 'SUN', 'SXP', 'TCT', 'TRB', 'TRX', 'VEN', 'VET', 
'WAN', 'WIN', 'WRX', 'WTC', 'XMR', 'XZC', 'ZEN', 'ZIL', 'HC', 'SC']


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
