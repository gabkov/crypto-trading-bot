import binance_bot
import medium_poller
import time
import telegram_channel
import market_tool
import data_handler


def get_average_runtime_from_list(lst):
    return sum(lst) / len(lst)

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
    
    runtime_list = []
    i = 0
    start = time.time()
    while True:
        i+= 1
        round = f"*** ROUND {i}.***"
        print(round)
        if i % 500 == 0:
            end = time.time()
            elapsed_time = end -start
            detailed_round = f"*** ROUND {i}. took {int(elapsed_time)} polling average: {get_average_runtime_from_list(runtime_list)} max: {max(runtime_list)} min: {min(runtime_list)}***"
            telegram_channel.send_message_to_me(detailed_round)
            start = time.time()
            runtime_list = []
        
        runtime_start = time.time()
        result = medium_poller.poll_titles_from_medium(new_ticker_list)
        runtime_end = time.time()
        runtime_duration = runtime_end - runtime_start
        runtime_list.append(runtime_duration)

        if result:
            binance_bot.handle_buy_order(result)
            break
        
        time.sleep(2)

    print("Bot succesfully finished")
    telegram_channel.send_message_to_me("LETS GO TO THE MOOOOOON!!!!")