import json, psycopg2

from flask import Flask, render_template, g
from flask_restful import Resource, Api

from query import Prices

app = Flask(__name__)
app.config.from_pyfile('config.py')
api = Api(app)

prices_data = Prices()

@app.route('/')
def index():
    return render_template('index.html')

class LatestPrice(Resource):
    def get(self):
        data = json.loads(prices_data.get_prices_as_json())
        return data

api.add_resource(LatestPrice, '/api/latestprice')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


