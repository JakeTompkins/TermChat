class Message:
    def __init__(self, attributes={}):
        self.fromUser = attributes["User"]["RemarkName"] or attributes["User"]["NickName"]
        self.text = attributes["Text"]
