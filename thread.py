from message import Message


class Thread:
    def __init__(self, user):
        self.user = user
        self.id = user["AttrStatus"]
        self.messages = []
        self.new = True

    def add(self, msg):
        msg = Message(msg)
        self.messages.append(msg)

    def dump(self):
        return self.messages

    def mark_read(self):
        self.new = False

    def mark_new(self):
        self.new = True
