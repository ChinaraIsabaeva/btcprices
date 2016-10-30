#!/usr/bin/python3

import requests


class Exchange(object):
    def __init__(self, ticker_url):
        self.ticker_url = ticker_url
        self.price = 0

    def get_ticker(self):
        response = requests.get(self.ticker_url)
        return response

    def reponse_as_json(self, response):
        return response.json()


class Bitfinex(Exchange):
    def __init__(self):
        self.ticker_url = 'https://api.bitfinex.com/v1/pubticker/BTCUSD'
        
    def get_latest_price(self):
        response = self.get_ticker()
        if response.ok:
            self.price = self.reponse_as_json['last_price']
        return self.price


class Bitstamp(Exchange):
    def __init__(self):
        self.ticker_url = 'https://www.bitstamp.net/api/ticker/'

    def get_latest_price(self):
        response = self.get_ticker()
        if response.ok:
            self.price = self.reponse_as_json['last']
        return self.price


class Okcoin(Exchange):
    def __init__(self):
        self.ticker_url = 'https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd'

    def get_latest_price(self):
        response = self.get_ticker()
        if response.ok:
            self.price = self.reponse_as_json['ticker']['last']
        return self.price

   
class Kraken(Exchange):
    def __init__(self):
        self.ticker_url = 'https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD'

    def get_latest_price(self):
        response = self.get_ticker()
        if response.ok:
            self.price = self.reponse_as_json['result']['XXBTZUSD']['c'][0]
        return self.price


class BTCE(Exchange):
    def __init__(self):
        self.ticker_url = 'https://btc-e.com/api/3/ticker/btc_usd'

    def get_latest_price(self):
        response = self.get_ticker()
        if response.ok:
            self.price = self.reponse_as_json['btc_usd']['last']
        return self.price


class Conibase(Exchange):
    def __init__(self):
        self.ticker_url = 'https://api.exchange.coinbase.com/products/BTC-USD/ticker'

    def get_latest_price(self):
        response = self.get_ticker()
        if response.ok:
            self.price = self.reponse_as_json['price']
        return self.price

