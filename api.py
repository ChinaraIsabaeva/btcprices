import json,  psycopg2, os
from urllib import parse
from psycopg2.extras import RealDictCursor

from flask import Flask, render_template
from flask_restful import Resource, Api

from lib.json_encoder import MyEncoder

app = Flask(__name__)
app.config.from_pyfile('config.py')
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

class LatestPrice(Resource):
    def get(self):
        connection = psycopg2.connect(app.config["DATABASE_URL"])
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT date, bitfinex, bitstamp, okcoin, kraken, btce, coinbase FROM (SELECT * FROM prices_history ORDER BY date desc LIMIT 1) as last order by id;")
        query = json.dumps(cursor.fetchall(), cls=MyEncoder)
        data = json.loads(query)
        connection.close()
        return data

api.add_resource(LatestPrice, '/api/latestprice')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=app.config["DEBUG"])


