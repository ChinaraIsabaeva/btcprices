import requests
import json

class Bitfinex:
    def __init__(self):
        self.url = 'https://api.bitfinex.com/v1'
        self.ticker = '/pubticker/BTCUSD'
    
    def get(self, url):
        url = self.url + url
        response = requests.get(url).text
        return response

    def get_latest_price(self):
        url = self.ticker
        response = self.get(url)
        str_to_json = json.loads(response)
        price = str_to_json['last_price']
        return price


class Bitstamp:
    def __init__(self):
        self.url = 'https://www.bitstamp.net/api'
        self.ticker = '/ticker/'

    def get(self, url, *params):
        url = self.url + url
        response = requests.get(url, verify=True).text
        return response

    def get_latest_price(self):
        url = self.ticker
        response = self.get(url)
        str_to_json = json.loads(response)
        price = str_to_json['last']
        return price


class Okcoin:
    def __init__(self):
        self.url = 'https://www.okcoin.com/api/v1'
        self.ticker = '/ticker.do?symbol=btc_usd'

    def get(self, url):
        url = self.url + url
        response = requests.get(url).text
        return response

    def get_latest_price(self):
        url = self.ticker
        response= self.get(url)
        str_to_json = json.loads(response)
        price =  str_to_json['ticker']['last']
        return price

   
class Kraken:
    def __init__(self):
        self.url = 'https://api.kraken.com/0/public'
        self.ticker = '/Ticker?pair=XXBTZUSD'

    def get(self, url):
        url = self.url + url
        response = requests.get(url).text
        return response

    def get_latest_price(self):
        url = self.ticker
        response = self.get(url)
        #str_to_json = json.loads(response)
        #price = str_to_json['result']['XXBTZUSD']['c'][0]
        return response
