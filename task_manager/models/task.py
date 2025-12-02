class Task: 
    def __init__(self, title, description, priority, deadline, status = "New"):
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.status = status

    def info(self):
        return f"Title: {self.title}\nDescription: {self.description}\nPriority: {self.priority}\nDeadline: {self.deadline}\nStatus: {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "deadline": self.deadline,
            "status": self.status
        }
    
    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            description=data["description"],
            priority=data["priority"],
            deadline=data["deadline"],
            status=data["status"]
        )
    
    