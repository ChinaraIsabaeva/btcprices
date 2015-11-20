#!/usr/bin/python3

import requests
import json

class Exchange(object):
    def __init__(self, ticker):
        self.ticker = ticker

    def get_ticker(self):
        response = requests.get(self.ticker)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        

class Bitfinex(Exchange):
    def __init__(self):
        self.ticker = 'https://api.bitfinex.com/v1/pubticker/BTCUSD'
        
    def get_latest_price(self):
        response = self.get_ticker()
        price = response['last_price']
        return price
   

class Bitstamp(Exchange):
    def __init__(self):
        self.ticker = 'https://www.bitstamp.net/api/ticker/'

    def get_latest_price(self):
        response = self.get_ticker()
        price = response['last']
        return price


class Okcoin(Exchange):
    def __init__(self):
        self.ticker = 'https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd'

    def get_latest_price(self):
        response= self.get_ticker()
        price =  response['ticker']['last']
        return price

   
class Kraken(Exchange):
    def __init__(self):
        self.ticker = 'https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD'

    def get_latest_price(self):
        response = self.get_ticker()
        price = response['result']['XXBTZUSD']['c'][0]
        return price
