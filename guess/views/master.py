from tornado.options import options

from guess.base import ModuleView, Controller
from guess.game_server import gamesrv


master_view = ModuleView('master')


@master_view.route("/")
class Home(Controller):
    def get(self):
        web_title = 'Guess'
        self.render("index.html", web_title=web_title)


@master_view.route('/main')
class Main(Controller):
    def get(self):
        username = self.get_cookie('username', default=None)
        if username is None:
            self.redirect('/')
        participants = gamesrv.participants
        max_participants = int(options.max_participants)
        if len(participants) == max_participants:
                gamesrv.start()
        web_title = 'Guess'
        self.render('guess.html', web_title=web_title, username=username)

    def post(self):
        username = self.get_argument('username', default=None)
        if username:
            self.set_cookie('username', username)
            participants = gamesrv.participants
            max_participants = int(options.max_participants)
            if (username not in participants and
                len(participants) < max_participants):
                gamesrv.add_participant(username)
            self.redirect('/main')
        else:
            self.write("Please input your name")


@master_view.route('/show')
class Show(Controller):
    def get(self):
        participants = gamesrv.participants
        self.write(str(options.max_participants))
        self.write(str(len(participants)))
        self.write(str(len(participants) < int(options.max_participants)))
