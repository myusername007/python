from models.password_store import PasswordStore

def main():
    store = PasswordStore()

    while True:
        print("\n1. Додати")
        print("2. Показати")
        print("3. Видалити")
        print("4. Вихід")

        choice = input("Вибір: ")

        if choice == "1":
            service = input("Сервіс: ")
            username = input("Логін: ")
            password = input("Пароль: ")
            store.add_entry(service, username, password)

        elif choice == "2":
            for item in store.list_entries():
                print(item)

        elif choice == "3":
            service = input("Що видалити (сервіс): ")
            store.delete_entry(service)

        elif choice == "4":
            break

if __name__ == "__main__":
    main()
