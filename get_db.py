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
