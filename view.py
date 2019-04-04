import os

import PIL


class View:
    def __init__(self):
        pass

    def update_history(self, messages):
        os.system("clear")
        for m in messages:
            print(f"{m.fromUser}: {m.text}")

    def select_user(self, users):
        os.system("clear")
        ind = 1
        for u in users:
            print(f"{ind}: {u['NickName']}")
            ind += 1
        return int(input("Enter an index: ")) - 1
