import bittrex_bot
import twitter_poller
import time

if __name__ == "__main__":
    print('Bot starting...')
    i = 0
    while True:
        i+= 1
        print(f"{i}. Polling segal twitter....")
        if twitter_poller.poll_tweets_from_user('@zosegal'):
            print("Found tweet at segals page.")
            bittrex_bot.go_all_in_on_dgb()
        print(f"{i}. Polling CB pro twitter....")
        if twitter_poller.poll_tweets_from_cb_pro():
            print("Found tweet at CoinbasePro page.")
            bittrex_bot.go_all_in_on_dgb()
        time.sleep(3)