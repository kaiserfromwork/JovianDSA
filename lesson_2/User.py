class User:

    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __str__(self):
        return f"User: {self.username}, name: {self.name} and email: {self.email}"
