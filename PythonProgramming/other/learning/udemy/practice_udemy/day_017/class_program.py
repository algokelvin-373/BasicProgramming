class User:
    def __init__(self, id, username): # Constructor Class User
        print('New User is Created')
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user): # Method in Class User
        user.followers += 1
        self.following += 1

user_1 = User("001", "Algokelvin")
print(f"User 1: {user_1.id} - {user_1.username}")

user_2 = User("002", "Andry")
print(f"User 2: {user_2.id} - {user_2.username}")

user_1.follow(user_2)
print(f"Followers User 1: {user_1.followers}")
print(f"Following User 1: {user_1.following}")
print(f"Followers User 2: {user_2.followers}")
print(f"Following User 2: {user_2.following}")