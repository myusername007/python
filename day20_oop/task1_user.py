class User():
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def is_adult(self):
        return self.age >= 18
    def __str__(self):
        return f"\nUsername: {self.username} \nemail: {self.email} \nage: {self.age}\n"
    
u = User("roma", "nutka.r@icloud.com", 21)
print(u)
print(f"18+ : {u.is_adult()}")