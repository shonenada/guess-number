#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os.path

from guess.modules import modules
from guess.util import config_from_file
from guess.base import Application


def app_root():
    """Return the root path of app"""
    app_root = os.path.dirname(os.path.realpath(__file__)) + '/'
    return app_root


def create_app(config_file=None):
    """Create app using factory method"""
    app = Application()

    if config_file:
        config_from_file(config_file)

    # database.bind_app(app)

    app.init_modules(modules)
    app.load_routes()

    app.deploy()

    return app
