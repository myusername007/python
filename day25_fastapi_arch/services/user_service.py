from storage.user_storage import add_user, get_all_users

def create_user(user):
    add_user(user)
    return user

def list_users():
    return get_all_users()