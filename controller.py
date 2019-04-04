from repo import Repo
from view import View


class Controller:
    def __init__(self):
        self.r = Repo()
        self.v = View()
        pass

    def add_message(self, msg, me=None):
        self.r.add_message(msg, me=me)
        messages = self.r.dump_current_thread()
        self.v.update_history(messages)

    def get_current_user(self):
        return self.r.current_thread.user

    def switch_thread(self, user):
        return self.r.switch_thread(user)

    def select_user(self, users):
        return self.v.select_user(users)

    def list_threads(self):
        threads = self.r.all_threads()
        self.v.list_threads(threads)
