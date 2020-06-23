import bittrex_bot
import twitter_poller
import time
import telegram_channel

if __name__ == "__main__":
    print('Bot starting...')
    i = 0
    while True:
        i+= 1
        round = f"*** ROUND {i}. ***"
        print(round)
        if i % 500 == 0:
            telegram_channel.send_message_to_me(round)
        print("Polling segal twitter....")
        if twitter_poller.poll_tweets_from_user('@zosegal'):
            print("Found tweet at segals page.")
            bittrex_bot.go_all_in_on_dgb()
        print("Polling CB pro twitter....")
        if twitter_poller.poll_tweets_from_cb_accounts('@CoinbasePro'):
            print("Found tweet at CoinbasePro page.")
            bittrex_bot.go_all_in_on_dgb()
        print("Polling Coinbase twitter....")
        if twitter_poller.poll_tweets_from_cb_accounts('@coinbase'):
            print("Found tweet at Coinbase page.")
            bittrex_bot.go_all_in_on_dgb()
        time.sleep(3)