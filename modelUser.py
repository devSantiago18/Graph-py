# User class


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
        self.adjacents = []

    def __str__(self) -> str:
        return f"Username: {self.username}. Password: {self.password}. Adjacents: {self.adjacents}"

    def to_list(self) -> list:
        l = list(self.adjacents)
        l.insert(0, self.password)
        l.insert(0, self.username)
        l.insert(0, self.id)
        return l
