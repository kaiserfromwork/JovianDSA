from UserDatabase import UserDatabase
from User import User

my_database = UserDatabase()
my_user_01 = User("user_01", "Lucas", "lucas@example.com")
my_user_02 = User("user_02", "Sacul", "sacul@example.com")

print(my_database.insert(my_user_01))
print(my_database.insert(my_user_01))
print(my_database.insert(my_user_02))
my_database.find("user_01")
my_database.update(my_user_01)


my_database_list = my_database.list_all()

print(my_database_list)

