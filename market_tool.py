import ccxt
import os

binance = ccxt.binance({ 'options': { 'adjustForTimeDifference': True }})
coinbase = ccxt.coinbasepro()

binance.apiKey = os.environ['BINANCE_PUBLIC_KEY']
binance.secret = os.environ['BINANCE_SECRET_KEY']
binance.checkRequiredCredentials()  # raises AuthenticationError
binance_markets = binance.load_markets()
coinbase_markets = coinbase.load_markets()

coinbase_coins = []

for key in coinbase_markets.keys():
    coinbase_coins.append(key.split('/')[0])

#print(coinbase_coins)

usdt_markets = []
for key in binance_markets.keys():
    if 'USDT' in key and 'UP' not in key and 'DOWN' not in key and 'BULL' not in key and 'BEAR' not in key:
        #usdt_markets.append(key)
        if 'HC' in key or 'SC' in key or 'HOT' in key:
            print(key)

        usdt_markets.append(key.split('/')[0])
#print(usdt_markets)

tickers = ['MATIC', 'OCEAN', 'STORJ', 'THETA', 'WAVES', 'DOGE', 'HBAR',
'IOST', 'IOTA', 'KAVA', 'LEND', 'NANO',  'PAXG', 'QTUM', 'ADA', 'ANT', 'BAL',
'BNT', 'BTS', 'BTT', 'CRV', 'DCR', 'DGB', 'DOT', 'ENJ', 'ERD',
'FET', 'HOT', 'ICX', 'JST', 'KMD', 'LSK', 'MFT', 'NEO', 'OGN', 'ONE',
'ONT', 'REN', 'RLC', 'RSR', 'RVN', 'SNX', 'SOL', 'SRM', 'STX', 'SXP', 'TRX',
'VET', 'XMR', 'ZEN', 'ZIL', 'SC']

print('############')
goldy = set(usdt_markets) - set(coinbase_coins)
goldy = list(goldy)

counter = 0
for ticker in tickers:
    if ticker in goldy:
        counter+=1

print()
print("Cointer: " + str(counter))
print()

goldy.sort()
goldy.sort(key=len, reverse=True)
filtered_goldy = list(filter(lambda x : "USD" not in x and "AUD" not in x and "GBP" not in x and "EUR" not in x and "BKRW" not in x, goldy))

print(filtered_goldy)
print(len(filtered_goldy))
