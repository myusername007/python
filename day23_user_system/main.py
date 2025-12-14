from services.user_service import create_user
from models.user import User
from storage import add_user, get_all_users

def main():
    user1 = create_user("Ivan", "ivan@example.com", 17)
    user2 = create_user("Roman", "roman@example.com", 21)

    add_user(user2)
    add_user(user1)
    print(get_all_users()) 

    
    print(f"Is {user1.username} an adult? {user1.is_adult()}")
    print(f"Is {user2.username} an adult? {user2.is_adult()}")

if __name__ == "__main__":
    main()
    


