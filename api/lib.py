import psycopg2, datetime, csv, os, decimal, json

from urllib import parse
from psycopg2.extras import RealDictCursor

from json_encoder import MyEncoder

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])

connection = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cursor = connection.cursor(cursor_factory=RealDictCursor)


def get_query_as_json():
    cursor.execute("SELECT date, bitfinex, bitstamp, okcoin, kraken FROM (SELECT * FROM prices_history ORDER BY date desc LIMIT 1) as last order by id;")
    date = json.dumps(cursor.fetchall(), cls=MyEncoder)
    return date
