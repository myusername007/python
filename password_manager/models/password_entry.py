class PasswordEntry:
    def __init__(self, service, username, password):
        self.service = service
        self.username = username
        self.password = password

    def info(self):
        return f"{self.service}: {self.username} / {self.password}"
