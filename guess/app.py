#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os.path

from guess.base import Application
from guess.utils import config_from_file
from guess.views.master import master_view
from guess.views.game import game_view


def app_root():
    """Return the root path of app"""
    app_root = os.path.dirname(os.path.realpath(__file__)) + '/'
    return app_root


def create_app(config_file=None):
    """Create app using factory method"""
    app = Application()

    if config_file:
        config_from_file(config_file)

    app.register_module(master_view)
    app.register_module(game_view)

    app.deploy()

    return app
