#!/usr/bin/python

import datetime, decimal, json


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%d %b %Y %H:%M:%S")
        elif isinstance(obj, decimal.Decimal):
            return str(obj)
        else:
            return super(MyEncoder, self).default(obj)
