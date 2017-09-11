#!/usr/bin/python3

import requests


class Exchange(object):
    def __init__(self):
        self.ticker_url = None
        self.price = 0

    def get_ticker(self):
        response = requests.get(self.ticker_url)
        return response

    def reponse_as_json(self, response):
        return response.json()


class Bitfinex(Exchange):
    def __init__(self):
        super(Bitfinex, self).__init__()
        self.ticker_url = 'https://api.bitfinex.com/v1/pubticker/BTCUSD'
        
    def get_latest_price(self):
        response = self.get_ticker()
        if response.ok:
            self.price = self.reponse_as_json(response)['last_price']
        return self.price


class Bitstamp(Exchange):
    def __init__(self):
        super(Bitstamp, self).__init__()
        self.ticker_url = 'https://www.bitstamp.net/api/ticker/'

    def get_latest_price(self):
        response = self.get_ticker()
        if response.ok:
            self.price = self.reponse_as_json(response)['last']
        return self.price


class Okcoin(Exchange):
    def __init__(self):
        super(Okcoin, self).__init__()
        self.ticker_url = 'https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd'

    def get_latest_price(self):
        response = self.get_ticker()
        if response.ok:
            self.price = self.reponse_as_json(response)['ticker']['last']
        return self.price

   
class Kraken(Exchange):
    def __init__(self):
        super(Kraken, self).__init__()
        self.ticker_url = 'https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD'

    def get_latest_price(self):
        response = self.get_ticker()
        if response.ok:
            self.price = self.reponse_as_json(response)['result']['XXBTZUSD']['c'][0]
        return self.price


class BTCE(Exchange):
    def __init__(self):
        super(BTCE, self).__init__()
        self.ticker_url = 'https://btc-e.com/api/3/ticker/btc_usd'

    def get_latest_price(self):
        response = self.get_ticker()
        if response.ok:
            self.price = self.reponse_as_json(response)['btc_usd']['last']
        return self.price


class Conibase(Exchange):
    def __init__(self):
        super(Conibase, self).__init__()
        self.ticker_url = 'https://api.gdax.com/products/BTC-USD/ticker'

    def get_latest_price(self):
        response = self.get_ticker()
        if response.ok:
            self.price = self.reponse_as_json(response)['price']
        return self.price

