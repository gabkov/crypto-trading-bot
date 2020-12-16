import binance_bot
import medium_poller
import time
import telegram_channel
import market_tool
import data_handler


if __name__ == "__main__":
    telegram_channel.send_message_to_me("<------- BOT STARTING ------->")
    print('Bot starting...')
    print("Refreshing ticker list...")
    old_ticker_list = data_handler.read_tickers_from_json()
    data_handler.refresh_tickers_and_dump()
    new_ticker_list = data_handler.read_tickers_from_json()
    new_coins = market_tool.get_new_coins(old_ticker_list, new_ticker_list)
    print(f"New coins added: {new_coins}")
    telegram_channel.send_message_to_me(f"Number of tickers loaded: {len(new_ticker_list)}")
    telegram_channel.send_message_to_me(f"New coins added: {new_coins}")
    telegram_channel.send_message_to_me(f"FULL TICKER LIST:\n{new_ticker_list}")
    
    i = 0
    start = time.time()
    round = f"*** ROUND {i}.***"
    while True:
        i+= 1
        print(round)
        if i % 1000 == 0:
            end = time.time()
            elapsed_time = end -start
            detailed_round = f"*** ROUND {i}. took {elapsed_time}***"
            telegram_channel.send_message_to_me(detailed_round)
            start = time.time()
        result = medium_poller.poll_titles_from_medium(new_ticker_list)
        if result:
            binance_bot.handle_buy_order(result)
            break
        
        time.sleep(1)

    print("Bot succesfully finished")
    telegram_channel.send_message_to_me("LETS GO TO THE MOOOOOON!!!!")