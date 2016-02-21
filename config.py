import os


if os.environ["ENV"] == "production":
    DOMAIN = "http://btcprices.info/"
    DEBUG = False
if os.environ["ENV"] == "staging":
    DOMAIN = "http://btcprices.herokuapp.com/"
    DEBUG = False
if os.environ["ENV"] == "development":
    DOMAIN = "http://127.0.0.1:5000/"
    DEBUG = True

DATABASE_URL = os.environ["DATABASE_URL"]
