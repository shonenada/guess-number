from guess.base import route
from guess.controller import Controller


@route("/")
class Home(Controller):
    def get(self):
        web_title = 'Tornado quick start on Heroku'
        app_name = 'Your app\'s name'
        self.render("index.html", web_title=web_title, app_name=app_name)
