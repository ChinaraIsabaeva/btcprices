import os

DOMAIN_PROD = "https://btcprices.herokuapp.com/"
DOMAIN_DEV = "http://127.0.0.1:5000/"


if os.environ["PROD"]:
    return DOMAIN_PROD
if os.environ["DEV"]:
    return DOMAIN_DEV
