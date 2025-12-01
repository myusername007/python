from .task import Task

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
    