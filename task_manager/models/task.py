class Task: 
    def __init__(self, title, description, priority, deadline, status = "New"):
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.status = status

    def info(self):
        return f"Title: {self.title}\nDescription: {self.description}\nPriority: {self.priority}\nDeadline: {self.deadline}\nStatus: {self.status}"

