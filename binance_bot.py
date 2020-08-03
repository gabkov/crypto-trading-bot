import ccxt
import os
import time
import telegram_channel

binance = ccxt.binance({ 'options': { 'adjustForTimeDifference': True }})
binance.apiKey = os.environ['BINANCE_PUBLIC_KEY']
binance.secret = os.environ['BINANCE_SECRET_KEY']
binance.checkRequiredCredentials()  # raises AuthenticationError
markets = binance.load_markets()

usdtdgb = binance.markets['DGB/USDT']


def get_crypto_balance(crypto):
    balance_list = binance.fetch_balance()['info']['balances']
    crypto_balance = [balance for balance in balance_list if balance['asset'] == crypto][0]
    free = crypto_balance['free']
    locked = crypto_balance['locked']
    total = float(free) + float(locked)
    print(f'{crypto} balance total: {int(total)}  Available: {free}')
    return crypto_balance


def cancel_all_open_order():
    open_orders = binance.fetch_open_orders(symbol="VET/USDT")
    for order in open_orders:
        order_id = order['id']
        print(f"Cancelling order {order_id}")
        binance.cancel_order(order_id, symbol=order["symbol"])


def get_ask_for_dgb():
    ask = binance.fetch_ticker('DGB/USDT')['ask']
    print(f'Current ask: {ask}' )
    return ask



def go_all_in_on_dgb():
    try:
        cancel_all_open_order()

        time.sleep(1)
        
        balance = float(get_crypto_balance('USDT')['free'])
        ask = get_ask_for_dgb()
        
        possible_buy_size = (balance / ask)
        
        if possible_buy_size > 1350:
            possible_buy_size -= 1000

        print(f"Will buy ~ {int(possible_buy_size)}")
        
        binance.create_market_buy_order('DGB/USDT', int(possible_buy_size))
        telegram_channel.send_message_to_me(f"Created market order at {ask} ~ {possible_buy_size}")

        print("All in to DGB BINANCE banx $$$$$$")

        if possible_buy_size <= 500:
            return
        else:
            go_all_in_on_dgb()

    except Exception as e:
        telegram_channel.send_message_to_me("EXCEPTION go_all_in_on_dgb():\n{}".format(e))
        if possible_buy_size <= 500:
            return
        go_all_in_on_dgb()


#get_crypto_balance("USDT")
#print(usddgb)
#print()
#print(bittrex.fetch_order_book("DGB/USD"))


#open_orders = binance.fetch_open_orders(symbol="VET/USDT")
#[print(order) for order in open_orders]
