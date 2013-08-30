#!/usr/bin/env python
#-*- coding: utf-8 -*-
import tornado.web
from tornado.options import options

from guess.settings import settings


class Application(tornado.web.Application):

    def __init__(self, modules=[], config={}):
        self.handlers = []
        self.modules = modules
        self.config = config

    def init_modules(self, modules=[]):
        self.modules = modules

    def load_routes(self):
        for module in self.modules:
            handler = (module.url, module)
            self.handlers.append(handler)

    def deploy(self):
        config = dict(self.config.items() + settings.items() +
                      options._options.items())
        tornado.web.Application.__init__(self, self.handlers, **config)


def route(url):
    """A decoration for app routes"""
    def handler(cls):
        cls.url = url
        return cls
    return handler
