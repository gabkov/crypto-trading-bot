import ccxt
import os

binance = ccxt.binance({ 'options': { 'adjustForTimeDifference': True }})
coinbase = ccxt.coinbasepro()

binance.apiKey = os.environ['BINANCE_PUBLIC_KEY']
binance.secret = os.environ['BINANCE_SECRET_KEY']
binance.checkRequiredCredentials()  # raises AuthenticationError
binance_markets = binance.load_markets()
coinbase_markets = coinbase.load_markets()

check_for_short_tickers = False
short_tickers = ['HC', 'SC', 'HOT']


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
    already_listed = {'PAX'}
    old_list = set(old_list)
    new_list = set(new_list) - already_listed
    return list(new_list - old_list)


coinbase_coins = get_coinbase_coins_list()
binance_usdt_pairs = get_binance_usdt_pairs()

print('############')
goldy = set(binance_usdt_pairs) - set(coinbase_coins)
goldy = list(goldy)

goldy.sort()
goldy.sort(key=len, reverse=True)
filtered_goldy = list(filter(lambda x : "USD" not in x and "AUD" not in x and "GBP" not in x and "EUR" not in x and "BKRW" not in x, goldy))

tickers = ['COCOS', 'MATIC', 'OCEAN', 'STORJ', 'STORM', 'STRAT', 'SUSHI', 'TFUEL', 'THETA', 
'WAVES', 'AION', 'ANKR', 'ARDR', 'ARPA', 'AVAX', 'BEAM', 'BZRX', 'CELR', 'COTI', 
'CTSI', 'CTXC', 'DATA', 'DENT', 'DOCK', 'DOGE', 'DREP', 'DUSK', 'EGLD', 'HBAR', 
'HIVE', 'IOST', 'IOTA', 'IOTX', 'IRIS', 'KAVA', 'LEND', 'LUNA', 'MITH', 'NANO', 
'NPXS', 'NULS', 'PAXG', 'PERL', 'QTUM', 'RUNE', 'SAND', 'STMX', 'STPT', 'TOMO', 
'TROY', 'VITE', 'VTHO', 'WING', 'WNXM', 'YFII', 'ADA', 'ANT', 'BAL', 'BCC', 'BEL', 
'BLZ', 'BNB', 'BNT', 'BSV', 'BTS', 'BTT', 'CHR', 'CHZ', 'COS', 'CRV', 'DCR', 'DGB', 
'DIA', 'DOT', 'ENJ', 'ERD', 'FET', 'FIO', 'FTM', 'FTT', 'FUN', 'GTO', 'GXS', 'HOT', 
'ICX', 'JST', 'KEY', 'KMD', 'KSM', 'LSK', 'LTO', 'MBL', 'MCO', 'MDT', 'MFT', 'MTL', 
'NBS', 'NEO', 'NKN', 'OGN', 'ONE', 'ONG', 'ONT', 'PNT', 'REN', 'RLC', 'RSR', 
'RVN', 'SNX', 'SOL', 'SRM', 'STX', 'SUN', 'SXP', 'TCT', 'TRB', 'TRX', 'VEN', 'VET', 
'WAN', 'WIN', 'WRX', 'WTC', 'XMR', 'XZC', 'ZEN', 'ZIL', 'HC', 'SC']

print(filtered_goldy)
print(len(tickers))
print(len(filtered_goldy))
new_ticker_list = get_new_coins(tickers, filtered_goldy)
print(f"New coins: {new_ticker_list}")