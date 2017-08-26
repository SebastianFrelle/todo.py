"""model class for todo list
"""


class TodoList:
    """Todo list

    Model class for todo list.
    """

    def __init__(self):
        self.list = []

    def add(self, item):
        """add new item and commit list"""
        self.list.append(item)

    def __getitem__(self, i):
        return self.list[i]

    def __setitem__(self, i, item):
        self.list[i] = item

    def __delitem__(self, i):
        del self.list[i]

    def __repr__(self):
        return self.list.__repr__()


class TodoItem:
    """Models an entry in the todo list.
    """

    def __init__(self, title, pri=None, done=False):
        self.title = title
        self.pri = pri
        self.done = done

    def __repr__(self):
        return f"{self.__class__.__name__}: \"{self.title}\", pri: {self.pri}"
