from tornado.web import UIModule

from guess.util import css_html, js_html


CSS_PATH = 'styles/'
JS_PATH = 'scripts/'


class Css_Mod(UIModule):
    def render(self, path):
        css_url = self.handler.static_url(CSS_PATH + path)
        return css_html(css_url)


class Js_Mod(UIModule):
    def render(self, path):
        js_url = self.handler.static_url(JS_PATH + path)
        return js_html(js_url)


class Css_Files_Mod(UIModule):
    def render(self, files=[]):
        html = ''
        for file in files:
            css_url = self.handler.static_url(CSS_PATH + file)
            html = ('%s%s%s' % (html, css_html(css_url), '\n'))
        return html[:-1]


class Js_Files_Mod(UIModule):
    def render(self, files=[]):
        html = ''
        for file in files:
            js_url = self.handler.static_url(JS_PATH + file)
            html = ('%s%s%s' % (html, js_html(js_url), '\n'))
        return html[:-1]


css = Css_Mod
js = Js_Mod
css_files = Css_Files_Mod
js_files = Js_Files_Mod
