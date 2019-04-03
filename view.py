import os


class View:
    def __init__(self):
        pass

    def update_history(self, messages):
        os.system("clear")
        for m in messages:
            print(f"{m.fromUser}: {m.text}")
