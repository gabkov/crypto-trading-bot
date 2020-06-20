import ccxt
import os

bittrex = ccxt.bittrex()
bittrex.apiKey = os.environ["PUBLIC_KEY"]
bittrex.secret = os.environ['SECRET_KEY']
bittrex.checkRequiredCredentials()  # raises AuthenticationError
markets = bittrex.load_markets()


def get_crypto_balance(crypto):
    balance_list = bittrex.fetch_balance()['info']
    crypto_balance = [balance for balance in balance_list if balance['Currency'] == crypto][0]
    print(f'{crypto} balance: {crypto_balance["Balance"]}  Available: {crypto_balance["Available"]}')
    return crypto_balance


get_crypto_balance("USD")
print()
print(bittrex, markets)