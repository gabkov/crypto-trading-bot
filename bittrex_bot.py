import ccxt
import os
import time

bittrex = ccxt.bittrex()
bittrex.apiKey = os.environ['PUBLIC_KEY']
bittrex.secret = os.environ['SECRET_KEY']
bittrex.checkRequiredCredentials()  # raises AuthenticationError
markets = bittrex.load_markets()

usddgb = bittrex.markets['DGB/USD']


def get_crypto_balance(crypto):
    balance_list = bittrex.fetch_balance()['info']
    crypto_balance = [balance for balance in balance_list if balance['Currency'] == crypto][0]
    print(f'{crypto} balance: {crypto_balance["Balance"]}  Available: {crypto_balance["Available"]}')
    return crypto_balance


def cancel_all_open_order():
    open_orders = bittrex.fetch_open_orders()
    for order in open_orders:
        order_id = order['id']
        print(f"Cancelling order {order_id}")
        bittrex.cancel_order(order_id)


def get_ask_for_dgb():
    ask = bittrex.fetch_ticker('DGB/USD')['ask']
    print(f'Current ask: {ask}' )
    return ask



def go_all_in_on_dgb():
    try:
        cancel_all_open_order()

        time.sleep(1)
        
        balance = get_crypto_balance('USD')['Available']
        ask = get_ask_for_dgb()
        
        possible_buy_size = (balance / ask)
        
        if possible_buy_size > 1350:
            possible_buy_size -= 1000
        
        if possible_buy_size < 300:
            return

        print(f"Will buy ~ {int(possible_buy_size)}")
        
       #bittrex.create_market_buy_order('DGB/USD', int(possible_buy_size))

        print("all in to DGB banx $$$$$$")
    except Exception:
        go_all_in_on_dgb()
    

#get_crypto_balance("USD")
#print(usddgb)
#print()
#print(bittrex.fetch_order_book("DGB/USD"))