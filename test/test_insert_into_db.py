import unittest, psycopg2, datetime

from app.get_prices import insert_into_db

connection = psycopg2.connect("dbname=test-btcPrices user=chinara")
cursor = connection.cursor()


class TestExhangesObjects(unittest.TestCase):

    def setUp(self):
        cursor.execute("CREATE TABLE prices_history (id SERIAL PRIMARY KEY, date TIMESTAMP, bitfinex DECIMAL(10,2), bitstamp DECIMAL(10,2), okcoin DECIMAL(10,2), kraken DECIMAL(10,2));")
        connection.commit()

    def tearDown(self):
        cursor.execute("drop table prices_history;")
        connection.commit()
        cursor.close()
        connection.close()

    def test_insert_into_db(self):
        insertion = insert_into_db()
        result = cursor.execute("SELECT * FROM prices_history;")
        print (result)


if __name__ == '__main__':
    unittest.main()
