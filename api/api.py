import json

from query import get_query_as_json

from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

class LatestPrice(Resource):
    def get(self):
        data = json.loads(get_query_as_json())
        return data

api.add_resource(LatestPrice, '/api/latestprice')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
