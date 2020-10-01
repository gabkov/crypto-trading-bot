import ccxt
import os

binance = ccxt.binance({ 'options': { 'adjustForTimeDifference': True }})
coinbase = ccxt.coinbasepro()

binance.apiKey = os.environ['BINANCE_PUBLIC_KEY']
binance.secret = os.environ['BINANCE_SECRET_KEY']
binance.checkRequiredCredentials()  # raises AuthenticationError
binance_markets = binance.load_markets()
coinbase_markets = coinbase.load_markets()


def get_coinbase_coins_list():
    coins = []
    for key in coinbase_markets.keys():
        coins.append(key.split('/')[0])
    return coins


def get_binance_usdt_pairs():
    usdt_pairs = []
    for key in binance_markets.keys():
        if 'USDT' in key and 'UP' not in key and 'DOWN' not in key and 'BULL' not in key and 'BEAR' not in key:
            usdt_pairs.append(key.split('/')[0])
    return usdt_pairs


def get_new_coins(old_list, new_list):
    old_list = set(old_list)
    new_list = set(new_list)
    new_coins = new_list - old_list
    return new_coins


def basic_filter_and_sort(goldy):
    goldy.sort()
    goldy.sort(key=len, reverse=True)
    return list(filter(lambda x : "USD" not in x and "AUD" not in x and "GBP" not in x and "EUR" not in x and "BKRW" not in x, goldy))


def get_ticker_list():
    coinbase_coins = get_coinbase_coins_list()
    binance_usdt_pairs = get_binance_usdt_pairs()
    already_listed = {'PAX', 'BAL', 'REN'}
    tickers = set(binance_usdt_pairs) - set(coinbase_coins)
    tickers = tickers - already_listed
    tickers = list(tickers)
    filtered_goldy = basic_filter_and_sort(tickers)
    return filtered_goldy
