import json
import datetime

from flask import Flask, render_template
from flask_restful import Resource, Api

from lib.exchanges import Bitfinex, Bitstamp, Kraken, Okcoin, BTCE, Conibase
from lib.json_encoder import MyEncoder

app = Flask(__name__)
app.config.from_pyfile('config.py')
api = Api(app)


@app.route('/')
def index():
    return render_template('index.html')


class LatestPrice(Resource):

    def get(self):
        bitfinex_latest_price = float(Bitfinex().get_latest_price())
        bitstamp_latest_price = float(Bitstamp().get_latest_price())
        okcoin_latest_price = float(Okcoin().get_latest_price())
        kraken_latest_price = float(Kraken().get_latest_price())
        coinbase_latest_price = float(Conibase().get_latest_price())

        initial_dict = {
            'date': datetime.datetime.now(),
            'coinbase': coinbase_latest_price,
            'kraken': kraken_latest_price,
            'bitstamp': bitstamp_latest_price,
            'okcoin': okcoin_latest_price,
            'bitfinex': bitfinex_latest_price
        }
        json_string = json.dumps(initial_dict, cls=MyEncoder)
        data = json.loads(json_string)
        return data


api.add_resource(LatestPrice, '/api/latestprice')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=app.config["DEBUG"])


