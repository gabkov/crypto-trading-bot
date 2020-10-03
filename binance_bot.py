import ccxt
import os
import time
import telegram_channel

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


def make_buy_order_for_symbol(symbol):
    pair = symbol + "/USDT"
    try:
        balance = get_free_usdt_balance()
        
        ask = get_ask_for_pair(pair)
        
        possible_buy_size = (balance / ask)
        
        buy_order = int(possible_buy_size * 0.99)
                
        binance.create_market_buy_order(pair, int(buy_order))
        
        telegram_channel.send_message_to_me(f"Created market order at {ask} ~ {buy_order} for {pair}")
    except Exception as e:
        print(e)
        telegram_channel.send_message_to_me("EXCEPTION make_buy_order_for_symbol():\n{}".format(e))