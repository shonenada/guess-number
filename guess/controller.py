#!/usr/bin/env python
#-*- coding: utf-8 -*-
import json
from datetime import date, datetime

import tornado.web


def __default(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(obj, date):
        return obj.strftime("%Y-%m-%d")
    else:
        raise TypeError("%r is not Json serializable" % obj)


def json_encode(obj):
    return json.dumps(obj, default=__default)


class Controller(tornado.web.RequestHandler):

    def get(self):
        raise tornado.web.HTTPError(405)

    def post(self):
        raise tornado.web.HTTPError(405)

    def put(self):
        raise tornado.web.HTTPError(405)

    def head(self):
        raise tornado.web.HTTPError(405)

    def delete(self):
        raise tornado.web.HTTPError(405)

    def json(self, obj):
        return json_encode(obj)
