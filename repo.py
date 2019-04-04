from thread import Thread


class Repo:
    def __init__(self):
        self.unread = []
        self.threads = []
        self.current_thread = None

    def add_message(self, msg, me=None):
        user = msg["User"]
        user_thread_arr = [
            thread for thread in self.threads if thread.user == user]
        if len(user_thread_arr) == 0:
            user_thread = Thread(user)
            self.threads.append(user_thread)
        else:
            user_thread = user_thread_arr[0]

        if me:
            msg["User"] = me
        user_thread.add(msg)
        if not user_thread == self.current_thread:
            user_thread.mark_new()

    def switch_thread(self, user):
        threads = [thread for thread in self.threads if thread.id ==
                   user["AttrStatus"]]
        if len(threads) > 0:
            self.current_thread = threads[0]
        else:
            self.current_thread = Thread(user)
            self.threads.append(self.current_thread)
        self.current_thread.mark_read()
        return self.current_thread.dump()

    def dump_current_thread(self):
        if self.current_thread:
            return self.current_thread.dump()
        else:
            return []

    def all_threads(self):
        return self.threads
