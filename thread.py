from message import Message


class Thread:
    def __init__(self, user):
        self.user = user
        self.id = user["AttrStatus"]
        self.messages = []
        print(f"New Thread - User: {user}")

    def add(self, msg):
        msg = Message(msg)
        self.messages.append(msg)

    def dump(self):
        return self.messages
