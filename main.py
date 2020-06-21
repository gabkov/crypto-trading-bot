import bittrex_bot
import twitter_poller
import time

if __name__ == "__main__":
    print('Bot starting...')
    while True:
        print("Polling twitter....")
        if twitter_poller.poll_tweets():
            bittrex_bot.go_all_in_on_dgb()
        time.sleep(5)