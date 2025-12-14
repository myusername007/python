class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def is_adult(self):
        return self.age >= 18
    
    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}', age={self.age})"
    
    
