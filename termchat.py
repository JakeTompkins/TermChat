import re
from threading import Thread
from bot import Bot

from view import View
v = View()

b = Bot()
me = b.me
t1 = Thread(target=b.run)

FIND_FRIEND = re.compile("^ff")
SEND_TEXT = re.compile("^st")


def capture_input():
    while True:
        cmd = input()
        if FIND_FRIEND.search(cmd):
            name = re.compile("(?<=^ff\s).+").search(cmd).group(0)
            messages = b.find_friend(name)
            v.update_history(messages)

        elif SEND_TEXT.search(cmd):
            msg = re.compile("(?<=^st\s).+").search(cmd).group(0)
            if msg == "-":
                continue
            else:
                b.send_text(msg)
                v.update_history(messages)


t2 = Thread(target=capture_input)

t1.start()
t2.start()
