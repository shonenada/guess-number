#!/usr/bin/env python
#-*- coding: utf-8 -*-
import tornado.web
from tornado.options import options

from guess.utils import json_encode 
from guess.settings import settings


class Route(object):

    def __init__(self, app):
        self.app = app 
    
    def __call__(self, url):
        def view_class(cls):
            self.app.handlers.append((url, cls))
            return cls
        return view_class 


class Application(tornado.web.Application):

    def __init__(self, modules=[], config={}):
        self.handlers = []
        self.modules = modules
        self.config = config
        self.route = Route(self)

    def register_module(self, module):
        for hdle in module.handlers:
            self.handlers.append(hdle)

    def deploy(self):
        config = dict(self.config.items() + settings.items() +
                      options._options.items())
        tornado.web.Application.__init__(self, self.handlers, **config)


class ModuleView(object):
    
    def __init__(self, name):
        self.name = name
        self.handlers = []
        self.route = Route(self)


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
