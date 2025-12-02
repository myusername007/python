from .task import Task
import json



class TaskStore:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, priority, deadline, status="New"):
        newtask = Task(title, description, priority, deadline, status)
        self.tasks.append(newtask)

    def list_tasks(self):
        return [t.info() for t in self.tasks]
    
    def delete_task(self, title):
        self.tasks = [t for t in self.tasks if t.title != title]

    def update_status(self, title, new_status):
        for t in self.tasks:
            if t.title == title:
                t.status = new_status
                break
    
    def update_priority(self, title, new_priority):
        for t in self.tasks:
            if t.title == title:
                t.priority = new_priority
                break
    
    def save_to_file(self, filename):
        try: 
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump([t.to_dict() for t in self.tasks], f, ensure_ascii=False, indent=4)
                f.write('\n')
        except FileNotFoundError:
            print("Помилка завантаження файлу.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
        except FileNotFoundError:
            print("Файл не знайдено. Починаємо з порожнього списку задач.")
        except json.JSONDecodeError:
            print("Помилка читання файлу. Починаємо з порожнього списку задач.")    

        