import binance_bot
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
        if i % 1000 == 0:
            telegram_channel.send_message_to_me(round)
        print("Polling CB pro twitter....")
        result = twitter_poller.poll_tweets_from_cb_accounts('@CoinbasePro')
        if result:
            symbol = result[0]
            print("Found tweet at CoinbasePro page.")
            binance_bot.make_buy_order_for_symbol(symbol)
            break
        
        time.sleep(1)

    print("Bot succesfully finished")
    telegram_channel.send_message_to_me("LETS GO TO THE MOOOOOON!!!!")