class UserDatabase:

    def __init__(self):
        self.user_database = []

    def insert(self, user):
        if not self.user_database:
            self.user_database.append(user)
            return f'User: {user} added!'

        if self.find(user.username) is None:
            for index in range(len(self.user_database)):
                if user.username < self.user_database[index].username:
                    self.user_database.insert(index, user)
                    return f'User: {user} added!'
            self.user_database.append(user)
            return f'User: {user} added!'

        return f'User: {user} already exists'

    def find(self, username):
        for x in range(len(self.user_database)):
            if username == self.user_database[x].username:
                print("User found!")
                return self.user_database[x]

    def update(self, user):
        user_found = self.find(user.username)
        if user_found:
            user_found.name, user_found.email = user.name, user.email
            print("User Updated!")
        else:
            print("User not Found!")

    def list_all(self):
        return self.user_database  # Returns a list of the database
