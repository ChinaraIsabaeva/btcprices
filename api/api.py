import json
from psycopg2.extras import RealDictCursor

from flask import Flask, render_template, g
from flask_restful import Resource, Api

from json_encoder import MyEncoder
from app_db import get_db

app = Flask(__name__)
app.config.from_pyfile('config.py')
api = Api(app)


@app.route('/')
def index():
    return render_template('index.html')

class LatestPrice(Resource):
    def get(self):
        cursor = get_db().cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT date, bitfinex, bitstamp, okcoin, kraken FROM (SELECT * FROM prices_history ORDER BY date desc LIMIT 1) as last order by id;")
        query = json.dumps(cursor.fetchall(), cls=MyEncoder)
        data = json.loads(query)
        cursor.close()
        get_db().close()
        return data

api.add_resource(LatestPrice, '/api/latestprice')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


