from __future__ import print_function
import sys

import nose
import tornado
from tornado.options import options

from develop_tools.find import find
from develop_tools.clean import clean
from develop_tools.pep8 import pep8
from develop_tools.search import search

from guess.app import create_app
from guess.util import config_from_file
# from guess.extensions import database


cmds = ['-c', 'clean', '-p', 'pep8', '-s', 'search', '-ss', 'ssearch', 
        '-i', 'initdb', '-d', 'dropdb', '-t', 'test', '-r', 'run']


def init_app(conf="develop.conf"):

    def print_info():
        # print("-i/initdb -- create tables in database")
        # print("-d/dropdb -- drop all tables in database")
        print("-c/clean -- clean *.pyc")
        print("-p/pep8 -- check pep8")
        print("-t/test -- run nosetests")
        print("-r/run -- run debug mode")

    length = len(sys.argv)
    cmd = sys.argv[1]

    if length <= 1 and not cmd in cmds:
        print_info()

    # if length > 1 and (cmd == 'initdb' or cmd == '-i'):
    #     app = create_app(conf)
    #     database.create_tables()
    #     print("Initialize tables, Complete!")

    # if length > 1 and (cmd == 'dropdb' or cmd == '-d'):
    #     app = create_app(conf)
    #     database.drop_tables()
    #     print("Drop tables, Complete!")

    if length > 1 and (cmd == 'clean' or cmd == '-c'):
        clean("./guess")
        clean("./tests")
        print("Clean files, Complete!")

    if length > 1 and (cmd == 'pep8' or cmd == '-p'):
        pep8()

    if length > 1 and (cmd == 'test' or cmd == '-t'):
        with popen("nosetests") as sh:
            result = sh.read()
            print(result)

    if length > 1 and (cmd == 'run' or cmd == '-r'):
        app = create_app(conf)
        run_app(app)


def run_app(app):
    web_port = options.port if options.port else 8000
    if options.debug:
        print("Debug at port %s" % web_port)
    else:
        print("Run at port %s" % web_port)
    app.listen(web_port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    init_app()
