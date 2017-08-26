import re

class TodoList:
    @classmethod
    def load(cls, file):
        t = TodoList()

        with open(file, 'r') as f:
            lines = [line.rstrip('\n') for line in f.readlines()]

        t.list = [TodoItem(line) for line in lines]
        return t

    def __init__(self):
        self.list = []

    def add(self, item):
        return self.list.append(item)

    def open_tasks(self):
        return [item for item in self.list if not item.done]

    def write(self, file):
        lines = [item.title for item in self.open_tasks()]
        with open(file, 'w') as f:
            f.write('\n'.join(lines))

    def items_of_pri(self, level):
        return [i for i in self.list if i.pri() == level]

    # Emulate list
    def __getitem__(self, i):
        return self.list[i]

    def __setitem__(self, i, item):
        self.list[i] = item


class TodoItem:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done
    
    def pri(self):
        m = re.findall(r'(?<=^\()[A-Z](?=\)\s', self.title)
        return m[0] if m else None

    def set_pri(self, level):
        self.depri()
        self.title = f'({level}) {self.title}'
    
    def depri(self):
        if self.pri() is not None:
            self.title = self.title[4:]


class TodoList:
    pass


