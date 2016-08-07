#!/usr/bin/python3

import psycopg2, datetime, csv, os

from urllib import parse
from psycopg2.extras import RealDictCursor

from exchanges import Bitfinex, Bitstamp, Kraken, Okcoin, BTCE, Conibase

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])

connection = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cursor = connection.cursor()


def insert_into_db():
    bitfinex_latest_price = float(0)
    bitstamp_latest_price = float(Bitstamp().get_latest_price())
    okcoin_latest_price = float(Okcoin().get_latest_price())
    kraken_latest_price = float(Kraken().get_latest_price())
    btce_latest_price = float(BTCE().get_latest_price())
    coinbase_latest_price = float(Conibase().get_latest_price())

    date = datetime.datetime.now()

    cursor.execute("INSERT INTO prices_history (date, bitfinex, bitstamp, kraken, okcoin, btce, coinbase) VALUES (%s, %s, %s, %s, %s, %s, %s)", (date, bitfinex_latest_price, bitstamp_latest_price, kraken_latest_price, okcoin_latest_price, btce_latest_price, coinbase_latest_price))
    connection.commit()


def save_to_file():
    with open('prices.csv', 'w') as csvfile:
       cursor.copy_expert("COPY prices_history TO STDOUT WITH CSV HEADER", csvfile) 

def main():
   insert_into_db()
   

if __name__ == '__main__':
    main()
    cursor.close()
    connection.close()


