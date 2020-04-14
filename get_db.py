#!/usr/bin/python

import os
import psycopg2

from urllib import parse


def get_db():
    url = parse.urlparse(os.environ["DATABASE_URL"])
    connection = psycopg2.connect(
        database=url.path[1:],
        user=url.username, 
        password=url.password, 
        host=url.hostname,
        port=url.port )
    return connection
