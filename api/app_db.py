#!/usr/bin/python

import json, os, psycopg2
from urllib import parse
from psycopg2.extras import RealDictCursor

from json_encoder import MyEncoder

def get_db():
    url = parse.urlparse(os.environ["DATABASE_URL"])
    connection = psycopg2.connect(
        database=url.path[1:],
        user=url.username, 
        password=url.password, 
        host=url.hostname,
        port=url.port )
    return connection

def get_prices_as_json(self):
    cursor = self.get_db().cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT date, bitfinex, bitstamp, okcoin, kraken FROM (SELECT * FROM prices_history ORDER BY date desc LIMIT 1) as last order by id;")
    date = json.dumps(cursor.fetchall(), cls=MyEncoder)
    cursor.close()
    self.get_db().close()
    return date



