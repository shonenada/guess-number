import os.path

from guess import ui_module


app_root = os.path.dirname(__file__)


settings = {
    "template_path": os.path.join(app_root, "templates"),
    "static_path": os.path.join(app_root, "static/"),
    "xsrf_cookies": True,
    'xheaders': True,
    "login_url": "/auth/login",
    "autoescape": None,
    "ui_modules": ui_module,
}