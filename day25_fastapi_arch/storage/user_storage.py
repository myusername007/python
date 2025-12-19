_users = []

def add_user(user):
    _users.append(user)

def get_all_users():
    return _users

def get_user_by_id(user_id: int):
    for user in _users:
        if user.id == user_id:
            return user
    return None

def delete_user(user_id: int):
    global _users
    _users = [u for u in _users if u.id != user_id]
