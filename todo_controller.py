"""Controller module for Firebase/TodoList integration
"""
import pyrebase

from todo import TodoList, TodoItem


class TodoController:
    """CRUD controls for Firebase
    """

    def __init__(self, conf, cred):
        self.app = pyrebase.initialize_app(conf)
        self.auth = self.app.auth()
        self.user = self.auth.sign_in_with_email_and_password(
            cred['email'], cred['password']
        )
        self._db = None

    def database(self):
        """Instantiate and return database"""
        if self._db is None:
            self._db = self.app.database()

        return self._db

    def create(self):
        """Create a new list and push it to database"""
        online_list = FirebaseTodoModel(owner_id=self.user['localId'])
        res = self.database().child('lists').push(
            None, token=self.user['idToken'])
        online_list.uid = res['name']

        return online_list

    def read(self, list_name):
        """Read online list into local one"""
        res = self.database().child('lists').child(
            list_name).get(self.user['idToken'])


class FirebaseTodoModel:
    """TodoList model w/ Firebase metadata"""
    @classmethod
    def read(cls, data):
        """Map dictionary to todo list"""
        return cls(
            owner_id=data['owner_id'],
            tlist=[TodoItem(**item_data) for item_data in data['list']]
        )

    def __init__(self, owner_id, tlist=TodoList(), uid=None):
        self.owner_id = owner_id
        self.tlist = tlist
        self.uid = uid

    def to_dict(self):
        """Dictionary representation

        Return a dict representation of the list for use with the Firebase
        database.
        """
        return {
            'uid': self.tlist.uid.hex,
            'list': [{'pri': e.pri, 'title': e.title, 'done': e.done}
                     for e in self.tlist.list],
        }
