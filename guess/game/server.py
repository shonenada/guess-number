import random

from tornado.options import options


class GameServer(object):

    def __init__(self):
        self.observers = []
        self.messages = []
        self.participants = []
        self.number, self.turn, self.max, self.min = (0, 0, 0, 0)

    def listen(self, callback):
        self.observers.append(callback)

    def start(self):
        self._generate_num()
        self.send_message('Game start! Participants: %s' %
                          ", ".join(self.participants))
        self.send_message('Now is %s\'s turn, range: [%s, %s]' %
                          (self.now_turn(), str(self.min), str(self.max)))

    def _generate_num(self):
        if self.number == 0:
            self.max = int(options.max_number)
            self.min = int(options.min_number)
            self.number = int(random.uniform(self.min, self.max))

    def guess(self, num):
        correct = (num == self.number)
        if correct:
            self.number, self.turn, self.max, self.min = (0, 0, 0, 0)
        else:
            self.turn = self.turn + 1
            if num > self.number:
                self.max = num
            else:
                self.min = num
        return correct

    def now_turn(self):
        return self.participants[self.turn]

    def get_range(self):
        return (self.min, self.max)
    
    def add_participant(self, name):
        if len(self.participants) < options.max_participants:
            self.participants.append(name)
            self.send_message("%s has took part in this game" % name)

    def send_message(self, message):
        try:
            self.messages.append(message)
            [call(message) for call in self.observers]
        finally:
            self.observers = []
