# User class


class User:
    def __init__(self, username=None, password=None, next_node=None, _id=None):
        self.username = username
        self.password = password
        self.next_node = next_node
        self.id = _id

    def get_ids_current(self) -> dict:
        return {
            'id': self.id,
            'next': self.next
        }

    def __str__(self) -> str:
        return f'{self.username},{self.password},{self.id},{self.next_node}'
