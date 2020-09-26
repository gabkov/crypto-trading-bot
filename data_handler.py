import json
import market_tool


def refresh_tickers_and_dump():
    with open('tickers.json', 'w') as f:
        json.dump(market_tool.get_ticker_list(), f, ensure_ascii=False)

def read_tickers_from_json():
    with open('tickers.json') as data_file:
        data_loaded = json.load(data_file)
    return data_loaded
