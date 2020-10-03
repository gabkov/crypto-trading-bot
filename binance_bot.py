import ccxt
import os
import time
import telegram_channel

binance = ccxt.binance({ 'options': { 'adjustForTimeDifference': True }})
binance.apiKey = os.environ['BINANCE_PUBLIC_KEY']
binance.secret = os.environ['BINANCE_SECRET_KEY']
binance.checkRequiredCredentials()  # raises AuthenticationError
markets = binance.load_markets()


def get_crypto_balance(crypto):
    balance_list = binance.fetch_balance()['info']['balances']
    crypto_balance = [balance for balance in balance_list if balance['asset'] == crypto][0]
    return crypto_balance


def get_ask_for_pair(pair):
    ask = binance.fetch_ticker(pair)['ask']
    return ask


def make_buy_order_for_symbol(symbol):
    pair = symbol + "/USDT"
    try:
        balance = float(get_crypto_balance('USDT')['free'])
        
        ask = get_ask_for_pair(pair)
        
        possible_buy_size = (balance / ask)
        
        buy_order = int(possible_buy_size * 0.99)
                
        binance.create_market_buy_order(pair, int(buy_order))
        
        telegram_channel.send_message_to_me(f"Created market order at {ask} ~ {buy_order}")

        print(f"All in to {pair} on BINANCE banx $$$$$$")

    except Exception as e:
        print(e)
        telegram_channel.send_message_to_me("EXCEPTION go_all_in_on_dgb():\n{}".format(e))