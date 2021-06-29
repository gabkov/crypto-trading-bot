import ccxt
import os
import time
import telegram_channel
import datetime

binance = ccxt.binance({ 'options': { 'adjustForTimeDifference': True }})
binance.apiKey = os.environ['BINANCE_PUBLIC_KEY']
binance.secret = os.environ['BINANCE_SECRET_KEY']
binance.checkRequiredCredentials()  # raises AuthenticationError
markets = binance.load_markets()


def get_free_usdt_balance():
    return binance.fetch_free_balance()["USDT"]


def get_ask_for_pair(pair):
    ask = binance.fetch_ticker(pair)['ask']
    return ask


def handle_buy_order(symbols):
    pairs = [symbol + "/USDT" for symbol in symbols]
    free_balance = get_free_usdt_balance()
    for_buying = int(free_balance * 0.99)
    per_pair_buy_size = for_buying / len(symbols)
    make_buy_order_for_pairs(pairs, per_pair_buy_size)


def make_buy_order_for_pairs(pairs, per_pair_buy_size):
    for pair in pairs:
        try:
            ask = get_ask_for_pair(pair)
            buy_order = (per_pair_buy_size / ask)
            #binance.create_market_buy_order(pair, int(buy_order))
            binance.create_market_buy_order(pair, 50)
        except Exception as e:
            print(e)
            telegram_channel.send_message_to_me(f"EXCEPTION make_buy_order_for_pairs():\n{pair}\n{e}")
    done = datetime.datetime.now()
    telegram_channel.send_message_to_me(f"{done}: Created market order for pairs: {pairs} with ~ {per_pair_buy_size} USDT")
