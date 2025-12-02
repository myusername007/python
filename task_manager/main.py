import json
from models.task_store import TaskStore


def main():
    store = TaskStore()
    store.load_from_file('tasks.json')
    while True:
        print("\n1. Додати задачу")
        print("2. Показати всі")
        print("3. Змінити статус")
        print("4. Змінити пріоритет")
        print("5. Видалити задачу")
        print("6. Вихід")

        choice = input("Вибір: ")
        if choice == "6":
            print("До побачення!")
            break
        elif choice not in {"1", "2", "3", "4", "5"}:
            print("Невірний вибір, спробуйте ще раз.")
            continue
        elif choice == "1":
            title = input("Назва: ")
            description = input("Опис: ")
            priority = int(input("Пріоритет (1-5): "))
            deadline = input("Крайній термін (YYYY-MM-DD): ")
            status = input("Статус (непочата, в процесі, завершена): ")
            newtask = store.add_task(title, description, priority, deadline, status)
            store.save_to_file('tasks.json')
        elif choice == "2":
            tasks = store.list_tasks()
            if not tasks:
                print("Немає задач для показу.")
            for t in tasks:
                print("---")
                print(t)
                
        elif choice == "3":
            title = input("Назва задачі для зміни статусу: ")
            if title not in [t.title for t in store.tasks]:
                print("Задача не знайдена.")
                continue
            new_status = input("Новий статус (непочата, в процесі, завершена): ")
            store.update_status(title, new_status)
            store.save_to_file('tasks.json')
        elif choice == "4":
            title = input("Назва задачі для зміни пріоритету: ")
            if title not in [t.title for t in store.tasks]:
                print("Задача не знайдена.")
                continue
            new_priority = int(input("Новий пріоритет (1-5): "))
            store.update_priority(title, new_priority)
            store.save_to_file('tasks.json')
        elif choice == "5":
            title = input("Назва задачі для видалення: ")
            if title not in [t.title for t in store.tasks]:
                print("Задача не знайдена.")
                continue
            store.delete_task(title)
            store.save_to_file('tasks.json')
        
if __name__ == "__main__":
    main()