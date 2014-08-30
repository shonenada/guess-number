from __future__ import print_function
import sys

from tornado.options import options
import tornado.ioloop

from develop_tools.clean import clean
from develop_tools.pep8 import pep8
from develop_tools.search import search

from guess.app import create_app


cmds = ['-c', 'clean', '-p', 'pep8', '-s', 'search', '-ss', 'ssearch',
        '-i', 'initdb', '-d', 'dropdb', '-t', 'test', '-r', 'run']


def init_app(conf='development.conf'):

    def print_info():
        print('-r/run -- run the server')
        print('-p/pep8')
        print('-c/clean')
        print('-t/tests')

    length = len(sys.argv)
    if length <= 1:
        print_info()
    
    cmd = sys.argv[1]
    if not cmd in cmds:
        print_info()

    if cmd in ('-c', 'clean'):
        clean('./guess')
        clean('./tests')
        print('Clean files, completed!')

    if cmd in ('-p', 'pep8'):
        pep8()

    if cmd in ('-t', 'test'):
        with popen('nosetests') as sh:
            result = sh.read()
            print(result)

    if cmd in ('-r', 'run'):
        app = create_app(conf)
        run_app(app)


def run_app(app):
    web_port = 8000
    if options.debug:
        print('Debug at port %s' % web_port)
    else:
        print('Run at port %s' % web_port)

    app.listen(web_port)
    tornado.ioloop.IOLoop.instance().start()
        

if __name__ == '__main__':
    init_app()
