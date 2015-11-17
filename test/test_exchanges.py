import unittest

from app.exchanges import Bitfinex, Bitstamp, Okcoin, Kraken

class TestExhangesObjects(unittest.TestCase):

    def test_get_bitfinex_ticker(self):
        exchange_obj = Bitfinex()
        result = exchange_obj.get_latest_price()
        self.assertIsNotNone(result)

    def test_get_bitstamp_ticker(self):
        exchange_obj = Bitstamp()
        result = exchange_obj.get_latest_price()
        self.assertIsNotNone(result)
    
    def test_get_okcoin_ticker(self):
        exchange_obj = Okcoin()
        result = exchange_obj.get_latest_price()
        self.assertIsNotNone(result)

    def test_get_kraken_ticker(self):
        exchange_obj = Kraken()
        result = exchange_obj.get_latest_price()
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
    
