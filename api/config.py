import os


if os.environ["ENV"] == "production":
    DOMAIN = "https://btcprices.herokuapp.com/"
if os.environ["ENV"] == "development":
    DOMAIN = "http://127.0.0.1:5000/"

DATABASE = os.environ["DATABASE_URL"]
