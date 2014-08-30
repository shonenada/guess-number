import json
from datetime import date, datetime

from tornado.util import exec_in
from tornado.options import options, define
from tornado.web import RequestHandler


def config_from_file(path, final=True):
    config = {}
    with open(path) as f:
        exec_in(f.read(), config, config)
    for name in config:
        if not name in options._options:
            define(name)
        options._options[name].set(str(config[name]))


def css_html(path):
    html = '<link rel="stylesheet" type="text/css" href="%s" />' % path
    return html


def js_html(path):
    html = ('<script language="javascript" '
            'type="text/javascript" src="%s"></script>' % path)
    return html


def __default(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(obj, date):
        return obj.strftime("%Y-%m-%d")
    else:
        raise TypeError("%r is not Json serializable" % obj)


def json_encode(obj):
    return json.dumps(obj, default=__default)
