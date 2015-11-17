#!/usr/bin/python3

import psycopg2, datetime, csv

from exchanges import Bitfinex, Bitstamp, Kraken, Okcoin
connection = psycopg2.connect("dbname=btcPrices user=chinara")
cursor = connection.cursor()


def insert_into_db():
    bitfinex_latest_price = float(Bitfinex().get_latest_price())
    bitstamp_latest_price = float(Bitstamp().get_latest_price())
    okcoin_latest_price = float(Okcoin().get_latest_price())
    kraken_latest_price = float(Kraken().get_latest_price())

    date = datetime.datetime.now()

    cursor.execute("INSERT INTO prices_history (date, bitfinex, bitstamp, kraken, okcoin) VALUES (%s, %s, %s, %s, %s)", (date, bitfinex_latest_price, bitstamp_latest_price, kraken_latest_price, okcoin_latest_price))
    connection.commit()


def save_to_file():
    with open('prices.csv', 'w') as csvfile:
       cursor.copy_expert("COPY prices_history TO STDOUT WITH CSV HEADER", csvfile) 


def main():
   insert_into_db()
   save_to_file()
   

if __name__ == '__main__':
    main()
    cursor.close()
    connection.close()


