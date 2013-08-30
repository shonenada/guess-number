from tornado.web import asynchronous
from tornado.options import options

from guess.base import route
from guess.controller import Controller
from guess.extensions import gamesrv




@route('/guess')
class Guess(Controller):

    def prepare(self):
        self.max_participants = int(options.max_participants)
        name = self.get_cookie('name', default=None)
        if name is None:
            self.redirect('/', status=403)
            self.finish()
        participants = gamesrv.participants
        if (name not in participants):
            self.redirect('/')
        if len(participants) > self.max_participants:
            gamesrv.send_message('Full or you have took part in the game.')
            self.finish()

    @asynchronous
    def get(self):
        @gamesrv.listen
        def func(msg):
            msg = self.json({'msg': msg})
            try:
                self.finish(msg)
            except IOError:
                pass

    def post(self):
        name = self.get_cookie('name')
        guess_number = self.get_argument('number')
        if not len(gamesrv.participants) == self.max_participants:
            gamesrv.send_message('The number of participants is not enough.')
            return None
        if name == gamesrv.now_turn():
            correct = gamesrv.guess(guess_number)
            if correct:
                gamesrv.send_message("%s guess the number: %s, "
                                     "and it is correct!! Game Over!" %
                                     (name, str(guess_number)))
                return None
            else:
                max_num, min_num = gamesrv.get_range()
                gamesrv.send_message("%s guess number: %s,"
                                     "now the range of" "number is [%s, %s]" %
                                     (name, guess_number, min_num, max_num))
                return None
