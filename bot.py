from controller import Controller
from view import View
from repo import Repo
import itchat as i
from itchat.content import *


class Bot:
    def __init__(self):
        i.auto_login()
        self.r = Repo()
        self.c = Controller()
        self.me = i.search_friends()

    def chat_with(self, user):
        if user:
            return self.c.switch_thread(user)
        else:
            return []

    def send_text(self, text):
        target = self.c.get_current_user()
        target.send(text)
        self.c.add_message({"User": target, "Text": text}, me=self.me)

    def find_friend(self, name):
        possibilities = i.search_friends(name=name)
        if len(possibilities) > 0:
            ind = 1
            for p in possibilities:
                print(f"{ind}: {p['NickName']}")
                ind += 1
            index = int(input("Enter an index: ")) - 1
            user = possibilities[index]
        else:
            new_query = input("No friends found, enter new name: ")
            if new_query == "-" or new_query == "":
                return []
            else:
                return self.find_friend(new_query)
        return self.chat_with(user)

    def run(self):
        @i.msg_register(TEXT)
        def display_msg(msg):
            self.c.add_message(msg)

        i.run()


# Message format: {"from": UserName, "text": "some string"}
