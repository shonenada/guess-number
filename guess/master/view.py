from tornado.options import options

from guess.base import route
from guess.controller import Controller
from guess.extensions import gamesrv


@route("/")
class Home(Controller):
    def get(self):
        web_title = 'Guess'
        self.render("index.html", web_title=web_title)


@route('/main')
class Main(Controller):

    def get(self):
        name = self.get_cookie('name', default=None)
        if name is None:
            self.redirect('/')
        participants = gamesrv.participants
        max_participants = int(options.max_participants)
        if len(participants) == max_participants:
                gamesrv.start()
        web_title = 'Guess'
        self.render('guess.html', web_title=web_title)

    def post(self):
        name = self.get_argument('name', default=None)
        if name:
            self.set_cookie('name', name)
            participants = gamesrv.participants
            max_participants = int(options.max_participants)
            if (name not in participants and
                len(participants) < max_participants):
                gamesrv.add_participant(name)
            self.redirect('/main')
        else:
            self.write("Please input your name")


@route('/show')
class Show(Controller):
    def get(self):
        participants = gamesrv.participants
        self.write(str(options.max_participants))
        self.write(str(len(participants)))
        self.write(str(len(participants) < int(options.max_participants)))
