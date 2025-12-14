from services.auth_service import register_user
from config import APP_NAME

def main():
    user = register_user("roma", "roma@mail.com", 21)
    print(APP_NAME)
    print(user)
    print("Adult:", user.is_adult())

if __name__ == "__main__":
    main()
