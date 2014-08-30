from tornado.web import UIModule

from guess.utils import css_html, js_html


class StaticMod(UIModule):
    def render(self, path):
        static_url = self.handler.static_url(path)
        static_path = static_url.split('?', 1)[0]
        if static_path.endswith('js'):
            return js_html(static_url)
        if static_path.endswith('css'):
            return css_html(static_url)
        return static_url


static_url = StaticMod
