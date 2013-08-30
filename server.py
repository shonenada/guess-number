import tornado.httpserver
import tornado.options
from tornado.options import options, define

from guess.app import create_app


define("port", default=5000, help="run on the given port", type=int)


def run_app():
    tornado.options.parse_command_line()
    app = create_app("production.conf")
    web_port = options.port
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(web_port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    run_app()
